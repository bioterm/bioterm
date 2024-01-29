import redis

from ..core.config import REDIS_DB
from ..core.config import REDIS_HOST
from ..core.config import REDIS_PORT
from ..core.config import REDIS_PW
from ..core.config import REDIS_SSL_CA_CERTS
from ..core.config import REDIS_SSL_CERT_REQS
from ..core.config import REDIS_SSL_CERTFILE
from ..core.config import REDIS_SSL_ENABLE
from ..core.config import REDIS_SSL_KEYFILE

# from redis import asyncio as aioredis


def get_redis_connection() -> redis.StrictRedis:
    return redis.StrictRedis(
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
