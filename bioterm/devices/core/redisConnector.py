import os
import time

import redis
from dotenv import find_dotenv
from dotenv import load_dotenv

from ...common.core.config import getenv_boolean
from ...common.core.logger import get_module_logger

logger = get_module_logger(__name__)

env_path = find_dotenv()
if env_path:
    logger.debug(f"Loading from: {env_path}")
    load_dotenv(env_path)
else:
    print(".env file not found")

# # Load environment variables from a .env file
# load_dotenv()


class RedisConnector:
    # default attributes for base settings
    REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
    REDIS_DB = int(os.environ.get("REDIS_DB", 0))
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)

    # default attributes for SSL
    REDIS_SSL = getenv_boolean("REDIS_SSL")
    REDIS_SSL_CERT_REQS = os.environ.get("REDIS_SSL_CERT_REQS", "required")
    REDIS_SSL_CA_CERTS = os.environ.get("REDIS_SSL_CA_CERTS", None)
    REDIS_SSL_CERTFILE = os.environ.get("REDIS_SSL_CERTFILE", None)
    REDIS_SSL_KEYFILE = os.environ.get("REDIS_SSL_KEYFILE", None)

    # default timeout
    REDIS_TIMEOUT = int(os.environ.get("REDIS_TIMEOUT", 5))

    def __init__(
        self,
        host=None,
        port=None,
        db=None,
        password=None,
        ssl=None,
        ssl_cert_reqs=None,
        ssl_ca_certs=None,
        ssl_certfile=None,
        ssl_keyfile=None,
        timeout=None,
    ):
        self.connection = None
        # redis base settings
        self.host = host or self.REDIS_HOST
        self.port = port or self.REDIS_PORT
        self.db = db or self.REDIS_DB
        self.password = password or self.REDIS_PASSWORD

        # SSL settings
        self.ssl = ssl if ssl is not None else self.REDIS_SSL
        self.ssl_cert_reqs = ssl_cert_reqs or self.REDIS_SSL_CERT_REQS
        self.ssl_ca_certs = ssl_ca_certs or self.REDIS_SSL_CA_CERTS
        self.ssl_certfile = ssl_certfile or self.REDIS_SSL_CERTFILE
        self.ssl_keyfile = ssl_keyfile or self.REDIS_SSL_KEYFILE

        # timeout settings
        self.timeout = timeout or self.REDIS_TIMEOUT

    def connect(self):
        logger.debug("Connecting to redis...")
        while True:
            try:
                self.connection = redis.StrictRedis(
                    host=self.host,
                    port=self.port,
                    db=self.db,
                    password=self.password,
                    ssl=self.ssl,
                    ssl_cert_reqs=self.ssl_cert_reqs,
                    ssl_ca_certs=self.ssl_ca_certs,
                    ssl_certfile=self.ssl_certfile,
                    ssl_keyfile=self.ssl_keyfile,
                )
                self.connection.ping()
                break
            except redis.exceptions.ConnectionError:
                logger.warning(
                    f"Failed to connect to Redis. Retrying in {self.timeout} seconds..."
                )
                time.sleep(self.timeout)

        return self.connection
