import time

from ...common.core.logger import get_module_logger
from ..core.redis_connector import get_redis_connection


STREAM_NAME = "telemetrystream"
CONSUMER_GROUPS = ["wsworker_group", "centralcontrol"]

logger = get_module_logger(__name__)

r = get_redis_connection()


def cleanup_stream():
    while True:
        messages = r.xrange(STREAM_NAME, min="-", max="+", count=1000)
        ids_to_delete = []

        for message_id, _ in messages:
            all_acknowledged = True

            for group in CONSUMER_GROUPS:
                pending = r.xpending_range(
                    STREAM_NAME, group, min=message_id, max=message_id, count=1
                )
                if pending:
                    all_acknowledged = False
                    break

            if all_acknowledged:
                ids_to_delete.append(message_id)
            else:
                # Stop as soon as a message not acknowledged by all consumers is found
                break

        if ids_to_delete:
            r.xdel(STREAM_NAME, *ids_to_delete)
            logger.debug(
                f"Deleted {len(ids_to_delete)} of {len(messages)} fetched messages. "
                f"First {message_id=}"
            )

        time.sleep(1)


def main():
    cleanup_stream()


if __name__ == "__main__":
    main()
