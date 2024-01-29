import asyncio
import json
from typing import List

from pydantic import ValidationError
from redis import asyncio as aioredis

from ...common.control.conditions import evaluate_condition
from ...common.core.logger import get_module_logger
from ...common.models.control.base_models import AllDevicesLastStatus
from ...common.models.control.base_models import DeviceLastStatus
from ...common.models.rpc.base_models import RPCPayload
from ...common.models.rules.base_models import Method
from ...common.models.rules.base_models import RulesDTO
from ...common.models.rules.base_models import RuleState
from ..core.config import REDIS_DB
from ..core.config import REDIS_HOST
from ..core.config import REDIS_PORT
from ..core.config import REDIS_PW
from ..core.config import REDIS_SSL_CA_CERTS
from ..core.config import REDIS_SSL_CERT_REQS
from ..core.config import REDIS_SSL_CERTFILE
from ..core.config import REDIS_SSL_ENABLE
from ..core.config import REDIS_SSL_KEYFILE


logger = get_module_logger(__name__)

# The object that will hold the last status of all devices
all_devices_status = AllDevicesLastStatus(devices={})


async def fetch_synced_rules(redis_client: aioredis.StrictRedis):
    # Retrieve and deserialize the "synced_rules" key
    rules_json = await redis_client.get("synced_rules")
    rules_data = json.loads(rules_json) if rules_json is not None else []

    # Convert the data into a list of Rule objects
    return [RulesDTO(**rule) for rule in rules_data]


# async def fetch_rules_status(redis_client: aioredis.StrictRedis):
#     # Retrieve and deserialize the "synced_rules" key
#     rules_json = await redis_client.get("active_rules")
#     rules_data = json.loads(rules_json) if rules_json is not None else []

#     # Convert the data into a list of Rule objects
#     return [RuleStatus(**rule) for rule in rules_data]


async def init_rule_state(
    redis_client: aioredis.StrictRedis, synced_rules: List[RulesDTO]
):
    for rule in synced_rules:
        key = f"rule_state_{rule.uuid}"
        if not await redis_client.exists(key):
            await redis_client.set(key, RuleState().model_dump_json())


async def get_rule_state(redis_client: aioredis.StrictRedis, uuid: str) -> RuleState:
    serialized_rulestate = await redis_client.get(f"rule_state_{uuid}")
    return RuleState.model_validate_json(serialized_rulestate)


async def send_rpc_to_device(
    redis_client: aioredis.StrictRedis, device_uuid: str, rpc: RPCPayload
):
    try:
        logger.debug(f"Sending to device {device_uuid}: {rpc.key} -> {rpc.params} ")
        await redis_client.xadd(
            device_uuid,
            {"key": rpc.key, "params": json.dumps(rpc.params)},
        )
    except ValidationError as e:
        logger.error(f"Validation error when parsing to RPCPayload: {e}")


def method_to_rpc_payload(method: Method) -> RPCPayload:
    params = {arg.name: arg.value for arg in method.arguments}
    return RPCPayload(key=method.name, params=params)


async def process_telemetrystream(
    redis_client: aioredis.StrictRedis, stream_name: str, consumer_group: str
):
    # Create a consumer group if it doesn't exist
    try:
        await redis_client.xgroup_create(
            stream_name, consumer_group, id="0", mkstream=True
        )
    except aioredis.ResponseError as e:
        # Ignore error if the group already exists
        if "BUSYGROUP Consumer Group name already exists" not in str(e):
            raise

    # Check if the "rules" keys exist
    # for key in ["synced_rules", "active_rules"]:
    #     if not await redis_client.exists(key):
    #         # Create the "rules" key with an empty list if it doesn't exist
    #         await redis_client.set(key, json.dumps([]))

    if not await redis_client.exists("synced_rules"):
        # Create the "rules" key with an empty list if it doesn't exist
        await redis_client.set("synced_rules", json.dumps([]))

    synced_rules = await fetch_synced_rules(redis_client=redis_client)
    logger.debug(f"Initial load of synced rules: {synced_rules}")

    await init_rule_state(redis_client=redis_client, synced_rules=synced_rules)

    last_check_time = 0
    while True:
        current_time = asyncio.get_event_loop().time()
        if current_time - last_check_time > 1:
            new_rules = await fetch_synced_rules(redis_client)
            if new_rules != synced_rules:
                synced_rules = new_rules
                await init_rule_state(
                    redis_client=redis_client, synced_rules=synced_rules
                )
                logger.info("Rules updated")

            last_check_time = current_time

        messages = await redis_client.xreadgroup(
            consumer_group, "consumer", {stream_name: ">"}, count=10, block=100
        )
        for _, message_list in messages:
            for message_id, message_data in message_list:
                # Decode message id and data from bytes to a dictionary
                decoded_message_data = {
                    k.decode("utf-8"): v.decode("utf-8")
                    for k, v in message_data.items()
                }
                decoded_message_id = message_id.decode("utf-8")

                # Extract the uuid from the decoded message data
                uuid = decoded_message_data.get("uuid", None)
                measurement = decoded_message_data.get("value", None)
                # TODO: this should be reworked, by changing the measurement classes
                if measurement:
                    try:
                        # Convert the JSON string to a dictionary
                        measurement_dict = json.loads(measurement)

                        # Extract timestamp from the measurement dictionary
                        timestamp = measurement_dict.pop("timestamp", None)

                        # Check if uuid is already present in the devices dictionary
                        if uuid not in all_devices_status.devices:
                            # If not, create a new DeviceLastStatus instance
                            all_devices_status.devices[uuid] = DeviceLastStatus(
                                name=uuid,
                                timestamp=timestamp,
                                last_id=decoded_message_id,
                                meas={},
                            )

                        # Update the timestamp and redis_id for the device
                        all_devices_status.devices[uuid].timestamp = timestamp
                        all_devices_status.devices[uuid].last_id = decoded_message_id

                        # Iterate over the remaining items in the measurement dictionary
                        for meas_name, meas_value in measurement_dict["meas"].items():
                            # Update the measurement values for the device
                            all_devices_status.devices[uuid].meas[
                                meas_name
                            ] = meas_value
                    except json.JSONDecodeError:
                        logger.error("Invalid JSON format for measurement")

                # Serialize the all_devices_status object to a JSON string
                all_devices_status_json = json.dumps(
                    all_devices_status,
                    default=lambda o: o.__dict__,  # Converts the object to a dictionary
                    sort_keys=True,
                    indent=4,
                )

                # Store the JSON string in Redis with a unique key
                await redis_client.set(
                    "all_devices_status_key", all_devices_status_json
                )

                # Acknowledge the message in the Redis stream
                await redis_client.xack(stream_name, consumer_group, message_id)

                for rule in synced_rules:
                    state = await get_rule_state(
                        redis_client=redis_client, uuid=rule.uuid
                    )
                    update_state = False
                    if evaluate_condition(rule.trigger_condition, all_devices_status):
                        if not state.active:
                            logger.info(f"Rule triggered: {rule}")
                            update_state = True
                            state.active = True
                            rpc = method_to_rpc_payload(rule.trigger_method)
                            await send_rpc_to_device(
                                redis_client=redis_client,
                                device_uuid=rule.device,
                                rpc=rpc,
                            )
                    if evaluate_condition(rule.release_condition, all_devices_status):
                        if state.active:
                            logger.info(f"Rule released: {rule}")
                            update_state = True
                            state.active = False
                            rpc = method_to_rpc_payload(rule.release_method)
                            await send_rpc_to_device(
                                redis_client=redis_client,
                                device_uuid=rule.device,
                                rpc=rpc,
                            )
                    if update_state:
                        await redis_client.set(
                            f"rule_state_{rule.uuid}", state.model_dump_json()
                        )


async def process_wsstream(
    redis_client: aioredis.StrictRedis, stream_name: str, consumer_group: str
):
    # Create a consumer group if it doesn't exist
    try:
        await redis_client.xgroup_create(
            stream_name, consumer_group, id="0", mkstream=True
        )
    except aioredis.ResponseError as e:
        # Ignore error if the group already exists
        if "BUSYGROUP Consumer Group name already exists" not in str(e):
            raise

    while True:
        messages = await redis_client.xreadgroup(
            consumer_group, "consumer", {stream_name: ">"}, count=10, block=100
        )
        for _, message_list in messages:
            for message_id, message_data in message_list:
                # Decode message id and data from bytes to a dictionary
                decoded_message_data = {
                    k.decode("utf-8"): v.decode("utf-8")
                    for k, v in message_data.items()
                }
                # decoded_message_id = message_id.decode("utf-8")

                # Extract the uuid from the decoded message data
                uuid = decoded_message_data.get("uuid", None)
                try:
                    rpc = RPCPayload.model_validate_json(
                        decoded_message_data.get("rpc", None)
                    )
                    logger.debug(
                        f"Sending to device {uuid}: {rpc.key} -> {rpc.params} "
                    )
                    await redis_client.xadd(
                        uuid,
                        {"key": rpc.key, "params": json.dumps(rpc.params)},
                    )
                except ValidationError as e:
                    logger.error(f"Validation error when parsing to RPCPayload: {e}")


async def main():
    # Connect to Redis
    redis_client = aioredis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PW,
        ssl=REDIS_SSL_ENABLE,
        ssl_ca_certs=REDIS_SSL_CA_CERTS,
        ssl_certfile=REDIS_SSL_CERTFILE,
        ssl_keyfile=REDIS_SSL_KEYFILE,
        ssl_cert_reqs=REDIS_SSL_CERT_REQS,
    )

    # Run the process stream coroutine for both streams
    await asyncio.gather(
        process_telemetrystream(redis_client, "telemetrystream", "centralcontrol"),
        process_wsstream(redis_client, "ws_incoming", "centralcontrol"),
    )

    redis_client.close()
    await redis_client.wait_closed()


# Run the main coroutine
asyncio.run(main())
