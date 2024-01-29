# from aioredis import Redis
from fastapi import Depends
from fastapi import FastAPI
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from ....common.core.logger import get_module_logger
from ..core.config import API_V0_STR
from ..core.config import AUTHENTIK_CLIENT_ID
from ..core.config import PROJECT_NAME
from ..core.config import REDIS_URL
from ..core.config import SECRET_KEY
from .api.api_v0.api import api_router

# from starlette.requests import Request

# from app.db.session import Session

logger = get_module_logger(__name__)


redis_pool = None


app = FastAPI(
    title=PROJECT_NAME,
    openapi_url="/api/v0/openapi.json",
    # docs_url=None,  # Disable docs (Swagger UI)
    redoc_url=None,  # Disable redoc
    swagger_ui_init_oauth={
        "clientId": AUTHENTIK_CLIENT_ID,
    },
)


@app.on_event("startup")
async def startup_event():
    global redis_pool
    # Create a connection pool to the Redis server
    redis_pool = await aioredis.from_url(REDIS_URL)

    # Ensure the stream exists
    if not await redis_pool.exists("server_ws_recv"):
        await redis_pool.xadd("server_ws_recv", {"message": "initial"})
        await redis_pool.xtrim("server_ws_recv", maxlen=0, approximate=False)

    logger.info("Finished startup...")


@app.on_event("shutdown")
async def shutdown_event():
    global redis_pool
    if redis_pool:
        await redis_pool.close()


def get_redis_pool():
    return redis_pool


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.include_router(
    api_router, prefix=API_V0_STR, dependencies=[Depends(get_redis_pool)]
)
