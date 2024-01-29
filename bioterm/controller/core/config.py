import os

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
    logger.warning("No .env file found. Using default environment variables.")

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
REDIS_DB = int(os.environ.get("REDIS_DB", 0))
REDIS_PW = os.environ.get("REDIS_PW", None)

# default attributes for SSL
REDIS_SSL_ENABLE = getenv_boolean("REDIS_SSL")
REDIS_SSL_CERT_REQS = os.environ.get("REDIS_SSL_CERT_REQS", "required")
REDIS_SSL_CA_CERTS = os.environ.get("REDIS_SSL_CA_CERTS", None)
REDIS_SSL_CERTFILE = os.environ.get("REDIS_SSL_CERTFILE", None)
REDIS_SSL_KEYFILE = os.environ.get("REDIS_SSL_KEYFILE", None)

# default timeout
REDIS_TIMEOUT = int(os.environ.get("REDIS_TIMEOUT", 5))

CONTROLLER_UUID = os.environ.get("CONTROLLER_UUID", None)
CONTROLLER_APIKEY = os.environ.get("CONTROLLER_APIKEY", None)

API_DOMAIN = os.environ.get("API_DOMAIN", None)
