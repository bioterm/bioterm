# from dataclasses import dataclass
import json
import uuid
from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from redis import asyncio as aioredis
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from .......common.core.logger import get_module_logger
from .......common.models.controllers.database_models import ControllerModel
from .......common.models.devices.base_models import DeviceCreate
from .......common.models.devices.base_models import DeviceUpdate
from .......common.models.devices.database_models import DeviceModel
from .......common.models.grafana.database_models import PanelModel
from .......common.models.rpc.base_models import MessageFromServer
from .......common.models.rpc.base_models import RPCMessage
from .......common.models.rpc.base_models import RPCPayload
from .....core.config import SQLALCHEMY_DATABASE_URI
from ....core.dependencies import get_redis_pool
from ....core.logger import log_endpoint
from ....core.metadata import generate_metadata
from ...utils.security import credentials_noadmin_exception
from ...utils.security import User
from ...utils.security import validate

# from aioredis import Redis

# from .......common.models.rpc import RPCPayload


router = APIRouter()
logger = get_module_logger(__name__)


# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URI)  # set echo=True to increase verbosity
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()

# FastAPI application
app = FastAPI()


@router.post("/", tags=["devices"])
async def create_device(device: DeviceCreate, current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    new_uuid = str(uuid.uuid4())
    registration_date = datetime.now()
    new_device = DeviceModel(
        uuid=new_uuid, registration_date=registration_date, **device.dict()
    )
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    db.close()
    return new_device


@router.get("/", tags=["devices"])
async def read_device(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    devices = db.query(DeviceModel).all()
    # explicitly load json columns
    for device in devices:
        _ = device.parameters
        _ = device.measurement_model
        _ = device.rpc
    db.close()
    return devices


@router.put("/{device_id}", tags=["devices"])
async def update_device(
    device_id: int,
    device: DeviceUpdate,
    current_user: User = Depends(validate),
):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_device = db.query(DeviceModel).filter(DeviceModel.id == device_id).first()
    if not db_device:
        db.close()
        raise HTTPException(status_code=404, detail="Device not found")
    for key, value in device.dict().items():
        setattr(db_device, key, value)
    db.commit()
    db.close()
    return db_device


@router.delete("/{device_id}", tags=["devices"])
async def delete_device(device_id: int, current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_device = db.query(DeviceModel).filter(DeviceModel.id == device_id).first()
    if not db_device:
        db.close()
        raise HTTPException(status_code=404, detail="Device not found")

    # Drop table with name equal to DeviceModel.uuid
    table_name = str(db_device.uuid)
    try:
        db.execute(text(f'DROP TABLE "{table_name.lower()}"'))
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to drop table: {e}")

    db.delete(db_device)
    db.commit()
    db.close()
    return {"status": "success"}


@router.get("/metadata", tags=["devices"])
async def get_metadata(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    form_elements_create = generate_metadata(DeviceCreate)
    form_elements_update = generate_metadata(DeviceUpdate)

    # Generate column info based on APIKey SQLAlchemy model's columns
    columns = [
        {
            "name": column.name,
            "label": column.name.upper(),
            "field": column.name,
            "align": "left",
            "sortable": True if column.primary_key else False,
        }
        for column in DeviceModel.__table__.columns
    ]

    return {
        "formElementsUpdate": form_elements_update,
        "formElementsCreate": form_elements_create,
        "columns": columns,
    }


@router.get("/{device_uuid}/panels", tags=["devices"])
async def read_panels(device_uuid: str, current_user: User = Depends(validate)):
    db = SessionLocal()
    uuids_without_suffix = [
        group.split("_")[0]
        for group in current_user.groups
        if group.endswith(("_read", "_write"))
    ]
    controller_uuid = (
        db.query(ControllerModel)
        .join(DeviceModel, DeviceModel.controller_id == ControllerModel.id)
        .filter(DeviceModel.uuid == device_uuid)
        .first()
    )
    if (
        "authentik Admins" in current_user.groups
        or controller_uuid.uuid in uuids_without_suffix
    ):
        panels = (
            db.query(PanelModel)
            .join(DeviceModel, PanelModel.device_id == DeviceModel.id)
            .filter(DeviceModel.uuid == device_uuid)
            .all()
        )
        db.close()
    else:
        panels = []
    db.close()
    return panels


@router.post("/{device_uuid}/rpc", tags=["devices"])
@log_endpoint
async def rpc(
    device_uuid: str,
    payload: RPCPayload,
    request: Request,
    redis: aioredis = Depends(get_redis_pool),
    current_user: User = Depends(validate),
):
    db = SessionLocal()
    controller_instance = (
        db.query(ControllerModel)
        .join(DeviceModel, DeviceModel.controller_id == ControllerModel.id)
        .filter(DeviceModel.uuid == device_uuid)
        .first()
    )

    db.close()

    if not controller_instance:
        raise HTTPException(status_code=404, detail="Device not found")

    channel_name = f"rpc_channel:{controller_instance.uuid}"
    message = MessageFromServer(
        message=RPCMessage(
            type="rpc",
            controller=controller_instance.uuid,
            device=device_uuid,
            rpc=payload,
        )
    )
    await redis.publish(channel_name, json.dumps(message.dict()))
    return {"status": "success"}
