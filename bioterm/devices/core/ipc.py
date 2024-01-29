import json
import queue
import time

from pydantic import ValidationError

from ...common.core.logger import get_module_logger
from ...common.models.rpc.base_models import RPCPayload
from ..core.queues import DatapointQueue
from .redisConnector import RedisConnector

logger = get_module_logger(__name__)


class IPC:
    def __init__(self):
        self.redis_conn = RedisConnector().connect()
        # redis.StrictRedis(host="localhost", port=6379, db=0)

    def listen_to_stream(
        self,
        stream_name: str,
        task_queue: queue.Queue,
        return_queue: queue.Queue,
        callback,
    ):
        last_id = "0"
        logger.info("Start listening to stream")
        while True:
            messages = self.redis_conn.xread({stream_name: "$"}, count=1, block=0)
            # messages = self.redis_conn.xread({stream_name: last_id}, count=1, block=0)
            for _, message_list in messages:
                for message_id, message_data in message_list:
                    # Decode message id and data from bytes to a dictionary
                    decoded_message_data = {
                        k.decode("utf-8"): v.decode("utf-8")
                        for k, v in message_data.items()
                    }
                    logger.debug(f"Decoded message: {decoded_message_data}")
                    try:
                        # Parse the "params" field as a dictionary if it's a string
                        if isinstance(decoded_message_data.get("params"), str):
                            decoded_message_data["params"] = json.loads(
                                decoded_message_data["params"]
                            )

                        rpc = RPCPayload(**decoded_message_data)
                        result = callback(rpc)
                        logger.debug(f"{result}")
                        last_id = message_id
                        logger.debug(last_id)
                    except ValidationError as e:
                        logger.error(
                            f"Validation error when parsing to RPCPayload: {e}"
                        )

    def send_to_stream(
        self,
        stream_name: str,
        datapoint_queue: DatapointQueue,
        queue_timeout: int,
        uuid: str,
    ):
        while True:
            try:
                datapoint = (
                    datapoint_queue.get_nowait()
                )  # Non-blocking get from the queue
                if datapoint is None:  # Stop condition
                    break
                logger.debug(f"Got datapoint: {datapoint}")
                try:
                    self.redis_conn.xadd(
                        stream_name,
                        {"uuid": uuid, "value": datapoint.model_dump_json()},
                    )
                except Exception as e:
                    logger.error(
                        f"Exception thrown when adding datapoint to redis streams: {e}"
                    )
            except queue.Empty:
                # Handle the queue beeing empty
                time.sleep(queue_timeout)
            except Exception as e:
                logger.error(f"Error occured: {e}")

    def channel_exists(self, channel_name: str) -> bool:
        """Checks if a channel has active subscribers."""
        return channel_name.encode() in self.redis_conn.execute_command(
            "PUBSUB", "CHANNELS"
        )
