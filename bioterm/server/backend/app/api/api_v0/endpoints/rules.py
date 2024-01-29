import json
import uuid

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from pydantic import parse_obj_as
from redis import asyncio as aioredis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .......common.core.logger import get_module_logger
from .......common.models.controllers.database_models import ControllerModel
from .......common.models.rpc.base_models import MessageFromServer
from .......common.models.rpc.base_models import RulesMessage
from .......common.models.rules.base_models import RuleCreate
from .......common.models.rules.base_models import RulesDTO
from .......common.models.rules.base_models import RuleUpdate
from .......common.models.rules.database_models import RuleModel
from .....core.config import SQLALCHEMY_DATABASE_URI
from ....core.dependencies import get_redis_pool
from ....core.logger import log_endpoint
from ...utils.security import credentials_noadmin_exception
from ...utils.security import User
from ...utils.security import validate

# from aioredis import Redis

# from ....core.metadata import generate_metadata


router = APIRouter()
logger = get_module_logger(__name__)


# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URI)  # set echo=True to increase verbosity
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@router.post("/{controller_uuid}", tags=["rules"])
@log_endpoint
async def create_rule(
    controller_uuid: str,
    rule: RuleCreate,
    request: Request,
    current_user: User = Depends(validate),
):
    uuids_without_suffix = [
        group.split("_")[0]
        for group in current_user.groups
        if group.endswith(("_write"))
    ]
    if not (
        "authentik Admins" in current_user.groups
        or controller_uuid in uuids_without_suffix
    ):
        raise credentials_noadmin_exception
    db = SessionLocal()
    controller_id_result = (
        db.query(ControllerModel.id)
        .filter(ControllerModel.uuid == controller_uuid)
        .first()
    )
    # Check if a result was found
    if controller_id_result is not None:
        # Extract the id from the result
        controller_id = controller_id_result[0]
    else:
        db.close()
        raise HTTPException(status_code=404, detail="Controller not found")

    new_uuid = str(uuid.uuid4())
    new_rule = RuleModel(uuid=new_uuid, controller_id=controller_id, **rule.dict())
    logger.debug(new_rule.__dict__)
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)
    db.close()
    return new_rule


@router.get("/{controller_uuid}", tags=["rules"])
@log_endpoint
async def read_rule(
    controller_uuid: str, request: Request, current_user: User = Depends(validate)
):
    uuids_without_suffix = [
        group.split("_")[0]
        for group in current_user.groups
        if group.endswith(("_read", "_write"))
    ]
    if not (
        "authentik Admins" in current_user.groups
        or controller_uuid in uuids_without_suffix
    ):
        raise credentials_noadmin_exception
    db = SessionLocal()
    rules = (
        db.query(RuleModel)
        .join(ControllerModel, ControllerModel.id == RuleModel.controller_id)
        .all()
    )
    # explicitly load json columns
    for rule in rules:
        _ = rule.rule
    db.close()
    return rules


@router.put("/{controller_uuid}/{rule_uuid}", tags=["rules"])
async def update_rule(
    controller_uuid: str,
    rule: RuleUpdate,
    rule_uuid: str,
    current_user: User = Depends(validate),
):
    uuids_without_suffix = [
        group.split("_")[0]
        for group in current_user.groups
        if group.endswith(("_write"))
    ]
    if not (
        "authentik Admins" in current_user.groups
        or controller_uuid in uuids_without_suffix
    ):
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_rule = db.query(RuleModel).filter(RuleModel.uuid == rule_uuid).first()
    if not db_rule:
        db.close()
        raise HTTPException(status_code=404, detail="Rule not found")
    for key, value in rule.model_dump().items():
        setattr(db_rule, key, value)
    db.commit()
    db.close()
    return db_rule


@router.delete("/{controller_uuid}/{rule_uuid}", tags=["rules"])
async def delete_rule(
    controller_uuid: str, rule_uuid: str, current_user: User = Depends(validate)
):
    uuids_without_suffix = [
        group.split("_")[0]
        for group in current_user.groups
        if group.endswith(("_write"))
    ]
    if not (
        "authentik Admins" in current_user.groups
        or controller_uuid in uuids_without_suffix
    ):
        raise credentials_noadmin_exception
    db = SessionLocal()
    rule = db.query(RuleModel).filter(RuleModel.uuid == rule_uuid).first()
    if not rule:
        db.close()
        raise HTTPException(status_code=404, detail="Rule not found")
    db.delete(rule)
    db.commit()
    db.close()
    return {"status": "success"}


# @router.get("/metadata", tags=["rules"])
# async def get_metadata(current_user: User = Depends(validate)):
#     if "authentik Admins" not in current_user.groups:
#         raise credentials_noadmin_exception
#     form_elements_create = generate_metadata(DeviceCreate)
#     form_elements_update = generate_metadata(DeviceUpdate)

#     # Generate column info based on APIKey SQLAlchemy model's columns
#     columns = [
#         {
#             "name": column.name,
#             "label": column.name.upper(),
#             "field": column.name,
#             "align": "left",
#             "sortable": True if column.primary_key else False,
#         }
#         for column in DeviceModel.__table__.columns
#     ]

#     return {
#         "formElementsUpdate": form_elements_update,
#         "formElementsCreate": form_elements_create,
#         "columns": columns,
#     }


@router.get("/{controller_uuid}/sync", tags=["rules"])
@log_endpoint
async def sync_rules(
    controller_uuid: str,
    request: Request,
    current_user: User = Depends(validate),
    redis: aioredis = Depends(get_redis_pool),
):
    uuids_without_suffix = [
        group.split("_")[0]
        for group in current_user.groups
        if group.endswith(("_write"))
    ]
    if not (
        "authentik Admins" in current_user.groups
        or controller_uuid in uuids_without_suffix
    ):
        raise credentials_noadmin_exception

    db = SessionLocal()
    controller_id_result = (
        db.query(ControllerModel.id)
        .filter(ControllerModel.uuid == controller_uuid)
        .first()
    )
    # Check if a result was found
    if controller_id_result is None:
        db.close()
        raise HTTPException(status_code=404, detail="Controller not found")

    rules = (
        db.query(RuleModel.uuid, RuleModel.rule)
        .join(ControllerModel, ControllerModel.id == RuleModel.controller_id)
        .filter(RuleModel.sync)
        .all()
    )
    db.close()

    if rules is None:
        raise HTTPException(status_code=404, detail="No rules to sync")

    # Deserialize JSON data into Pydantic Rule objects
    pydantic_rules = [
        parse_obj_as(RulesDTO, {"uuid": uuid, **rule_data}) for uuid, rule_data in rules
    ]

    channel_name = f"rpc_channel:{controller_uuid}"
    message = MessageFromServer(
        message=RulesMessage(
            type="rules", controller=controller_uuid, rules=pydantic_rules
        )
    )
    await redis.publish(channel_name, json.dumps(message.dict()))
    return {"status": "success"}
