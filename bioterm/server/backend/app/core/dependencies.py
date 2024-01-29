# from aioredis import Redis
from redis import asyncio as aioredis


def get_redis_pool() -> aioredis:
    from ..main import redis_pool  # import it here to avoid cyclic imports

    return redis_pool
