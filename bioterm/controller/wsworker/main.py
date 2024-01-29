import asyncio
import json
import socket
import ssl
from typing import NoReturn

import redis
import websockets
from pydantic import ValidationError

from ...common.core.logger import get_module_logger
from ...common.models.rpc.base_models import RPCMessage
from ...common.models.rpc.base_models import RulesMessage
from ..core.config import API_DOMAIN
from ..core.config import CONTROLLER_APIKEY
from ..core.config import CONTROLLER_UUID
from ..core.redis_connector import get_redis_connection

# from ...common.models.rpc.base_models import MessageFromServer


logger = get_module_logger(__name__)

REDIS_READ_STREAM = "telemetrystream"
REDIS_WRITE_STREAM = "ws_incoming"
REDIS_GROUP_NAME = "wsworker_group"
REDIS_CONSUMER_NAME = "wsworker_consumer"
WS_ENDPOINT = f"wss://{API_DOMAIN}/api/v0/controller/{CONTROLLER_UUID}/ws"
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
headers = {"Authorization": f"Bearer {CONTROLLER_APIKEY}"}


async def websocket_worker(
    ws_uri: str, read_stream: str, write_stream: str
) -> NoReturn:
    """
    An asynchronous worker function that listens to a Redis stream and forwards messages
      to a WebSocket URI.

    This worker will first ensure the existence of the specified Redis stream and
    consumer group. It then continuously listens to the WebSocket connection, reads
    new messages from the Redis stream, and forwards them through the WebSocket. It
    handles connection interruptions and retries the connection.

    :param ws_uri: The WebSocket URI to connect to.
    :type ws_uri: str
    :param read_stream: The Redis stream's name to listen for messages.
    :type read_stream: str
    """

    # Initialize Redis client
    r = get_redis_connection()

    consumer_id = socket.gethostname()

    # Ensure the streams exist
    if not r.exists(read_stream):
        r.xadd(read_stream, {"message": "initial"})
        r.xtrim(read_stream, maxlen=0, approximate=False)

    if not r.exists(write_stream):
        r.xadd(write_stream, {"message": "initial"})
        r.xtrim(write_stream, maxlen=0, approximate=False)

    # Ensure the consumer group exists
    try:
        r.xgroup_create(read_stream, REDIS_GROUP_NAME, id="0", mkstream=True)
    except redis.exceptions.ResponseError as e:
        # Ignore error if the group already exists
        if "BUSYGROUP Consumer Group name already exists" not in str(e):
            raise

    # Main loop: handle WebSocket connection and messages forwarding
    while True:
        try:
            # Connect to the WebSocket
            async with websockets.connect(
                ws_uri,
                extra_headers=headers,
                ssl=ssl_context,
            ) as websocket:
                logger.info(f"Connected to websocket at: {ws_uri}")
                while True:
                    # Check for incoming messages briefly
                    try:
                        message_json = await asyncio.wait_for(
                            websocket.recv(), timeout=0.01
                        )
                        try:
                            # Ensure that the received message is a string
                            if not isinstance(message_json, str):
                                logger.error(
                                    f"Received message is not a string: {message_json}"
                                )
                                continue

                            message_data = json.loads(message_json)

                            # Extract the inner dictionary from the 'message' key
                            inner_message = message_data.get("message", {})

                            # Check the type and parse accordingly
                            if inner_message.get("type") == "rpc":
                                message = RPCMessage.model_validate(inner_message)
                                if isinstance(message, RPCMessage):
                                    rpc_data = json.dumps(message.rpc.model_dump())
                                    r.xadd(
                                        write_stream,
                                        {"uuid": message.device, "rpc": rpc_data},
                                    )
                            elif inner_message.get("type") == "rules":
                                message = RulesMessage.model_validate(inner_message)
                                if isinstance(message, RulesMessage):
                                    # Convert each Rule object into a dictionary
                                    rules_list = [r.dict() for r in message.rules]

                                    # Serialize the list of dictionaries to a JSON str
                                    rules_json = json.dumps(rules_list)

                                    r.set("synced_rules", rules_json)
                                    logger.debug(
                                        "Rules message received and stored in Redis"
                                    )
                                    pass

                        except ValidationError as e:
                            logger.error(
                                f"Validation error when parsing message "
                                f"to MessageFromServer: {e}"
                            )
                        except Exception as e:
                            logger.error(
                                f"Exception thrown when adding datapoint "
                                f"to redis streams: {e}"
                            )
                    except asyncio.TimeoutError:
                        pass  # No incoming message, pass to avoid blocking

                    # Get new messages from the stream
                    messages = r.xreadgroup(
                        REDIS_GROUP_NAME,
                        consumer_id,
                        {read_stream: ">"},
                        count=100,
                        block=100,
                    )

                    message_ids = []
                    send_coroutines = []

                    for _, message_list in messages:
                        for message_id, message_data in message_list:
                            # Send message over websocket
                            data = {
                                "id": message_id.decode("utf-8"),
                                "data": {
                                    k.decode("utf-8"): v.decode("utf-8")
                                    for k, v in message_data.items()
                                },
                            }
                            logger.debug(f"Sending message: {data}")
                            message_ids.append(message_id)
                            # await websocket.send(json.dumps(data))

                            # Add the send coroutine to the list
                            send_coroutines.append(websocket.send(json.dumps(data)))

                    # Use asyncio.gather to run all send coroutines in parallel
                    await asyncio.gather(*send_coroutines)

                    # Acknowledge all the messages at once in the Redis stream
                    if message_ids:
                        r.xack(read_stream, REDIS_GROUP_NAME, *message_ids)
                    else:
                        logger.debug("No new messages to acknowledge")

        except websockets.ConnectionClosed:
            # Handle closed connection and retry
            logger.warning("WebSocket connection closed. Retrying...")
            await asyncio.sleep(5)  # Optional: sleep for 5 seconds before retrying

        except websockets.InvalidStatusCode as e:
            # Handle rejected connection
            if e.status_code == 400:
                logger.error("Connection rejected. Terminating.")
                break  # Exit the loop to terminate the script
            if e.status_code == 403:
                logger.error(
                    "Connection rejected due to wrong credentials. Terminating..."
                )
                break  # Exit the loop to terminate the script

        except Exception as e:  # Handle other exceptions
            logger.error(f"Error occurred: {e}. Retrying...")
            await asyncio.sleep(5)


logger.info("Starting wsworker...")
loop = asyncio.get_event_loop()
loop.run_until_complete(
    websocket_worker(WS_ENDPOINT, REDIS_READ_STREAM, REDIS_WRITE_STREAM)
)
