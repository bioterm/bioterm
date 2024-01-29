from fastapi import APIRouter
from fastapi import Depends

from ...core.dependencies import get_redis_pool
from .endpoints import apikeys
from .endpoints import controller
from .endpoints import devices
from .endpoints import gdpr
from .endpoints import grafana
from .endpoints import rules

# from .endpoints import login
# from .endpoints import token
# from .endpoints import users


api_router = APIRouter()
# api_router.include_router(login.router)
api_router.include_router(
    controller.router, prefix="/controller", dependencies=[Depends(get_redis_pool)]
)
# api_router.include_router(users.router)
api_router.include_router(grafana.router, prefix="/grafana")
api_router.include_router(apikeys.router, prefix="/apikeys")
api_router.include_router(
    devices.router, prefix="/devices", dependencies=[Depends(get_redis_pool)]
)
api_router.include_router(gdpr.router, prefix="/gdpr")
api_router.include_router(rules.router, prefix="/rules")
# api_router.include_router(token.router)
