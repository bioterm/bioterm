# from dataclasses import dataclass
import asyncio
import csv
import io
import json
import typing
import uuid
import zipfile
from datetime import datetime
from datetime import timedelta
from typing import get_type_hints
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import WebSocket
from fastapi.responses import StreamingResponse
from fastapi.security.api_key import APIKey
from redis import asyncio as aioredis
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import not_
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from .......common.core.logger import get_module_logger
from .......common.core.responses import BACKEND_CONTROLLER_RESPONSES
from .......common.core.responses import BACKEND_DEVICE_RESPONSES
from .......common.models.apikeys.database_models import APIKeyModel
from .......common.models.controllers.base_models import ControllerCreate
from .......common.models.controllers.base_models import ControllerRegistration
from .......common.models.controllers.base_models import ControllerUpdate
from .......common.models.controllers.database_models import ControllerModel
from .......common.models.devices.base_models import DeviceRegistration
from .......common.models.devices.database_models import DeviceModel
from .......common.models.grafana.database_models import DashboardModel
from .......common.models.rules.database_models import RuleModel  # noqa: F401
from .....core.config import SQLALCHEMY_DATABASE_URI
from ....core.dependencies import get_redis_pool
from ....core.metadata import generate_metadata
from ....grafana.service import GrafanaService
from ...utils.security import credentials_noadmin_exception
from ...utils.security import get_api_key
from ...utils.security import get_api_key_ws
from ...utils.security import User
from ...utils.security import validate

# from aioredis import Redis

router = APIRouter()
logger = get_module_logger(__name__)

# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URI)  # set echo=True to increase verbosity
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# JSON to SQLAlchemy type mapping
TYPE_MAPPING = {"integer": Integer, "number": Float, "string": String}

# FastAPI application
app = FastAPI()


controllers_cache = []

TASK_EXPIRY_DURATION = timedelta(hours=1)


def is_valid_uuid(s: str) -> bool:
    try:
        uuid.UUID(s)
        return True
    except ValueError:
        return False


def is_optional_type(t: typing.Type) -> bool:
    """Check if a type is Optional[SomeType]."""
    origin = typing.get_origin(t)
    if origin is typing.Union:
        return type(None) in typing.get_args(t)
    return False


def devices_match(device: DeviceRegistration, registered_device: DeviceModel) -> bool:
    # Get the type hints for the DeviceRegistration class
    type_hints = get_type_hints(DeviceRegistration)

    # Determine which attributes are Optional
    optional_attrs = {k for k, v in type_hints.items() if is_optional_type(v)}

    # Convert the Pydantic model to a dictionary
    device_attributes = device.dict()

    for attr, value in device_attributes.items():
        # Skip the optional attributes
        if attr in optional_attrs:
            continue

        try:
            # Check if attribute exists in registered_device and compare values
            if getattr(registered_device, attr) != value:
                return False
        except AttributeError:
            # Handle cases where the attribute doesn't exist in registered_device
            return False

    # If all checks pass, the devices match
    return True


def create_table_from_json(metadata, table_name, meas_json_schema, prop_json_schema):
    table_name = table_name.lower()

    schema_prefixes = {"meas": meas_json_schema, "prop": prop_json_schema}

    columns = []
    columns.append(Column("timestamp", DateTime(timezone=True)))

    # for json_schema in [meas_json_schema, prop_json_schema]:
    for prefix, json_schema in schema_prefixes.items():
        properties = json_schema["properties"]

        for prop, details in properties.items():
            prefixed_prop = f"{prefix}_{prop}"
            # if prop == "timestamp":
            #     columns.append(Column(prop, DateTime(timezone=True)))
            #     continue

            if "$ref" in details:  # Handle referenced enum type
                enum_name = details["$ref"].split("/")[-1]
                enum_values = json_schema["$defs"][enum_name]["enum"]
                enum_type_name = f"{table_name}_{prefixed_prop}_enum"

                columns.append(
                    Column(prefixed_prop, Enum(*enum_values, name=enum_type_name))
                )
            else:
                type_name = details["type"]
                sqlalchemy_type = TYPE_MAPPING[type_name]

                columns.append(Column(prefixed_prop, sqlalchemy_type))  # , **kwargs
    return Table(table_name, metadata, *columns)


@router.on_event("startup")
def load_controllers():
    """Load controllers into cache at startup"""
    logger.debug("Retrieving controllers from database...")
    db = SessionLocal()

    controllers_infos = db.query(ControllerModel).all()
    for controller_info in controllers_infos:
        controllers_cache.append(controller_info)

    # Logging each controller's details separately
    for controller in controllers_cache:
        logger.debug(f"Controller [{controller.uuid}]")


@router.post("/register_controller", tags=["controllers"])
def register_controller(
    controller: ControllerRegistration, api_key: APIKey = Depends(get_api_key)
):
    if not is_valid_uuid(controller.uuid):
        raise HTTPException(**BACKEND_DEVICE_RESPONSES["REG_ERROR_UUIDFORMAT"])

    db = SessionLocal()

    registered_controller = (
        db.query(APIKeyModel)
        .join(ControllerModel, ControllerModel.id == APIKeyModel.controller_id)
        .filter(ControllerModel.uuid == controller.uuid)
        .filter(APIKeyModel.key == api_key)
        .first()
    )
    uuid_exists = (
        db.query(ControllerModel.id, ControllerModel.uuid)
        .filter_by(uuid=controller.uuid)
        .first()
    )
    claimed_api_keys = (
        db.query(APIKeyModel)
        .join(ControllerModel, ControllerModel.id == APIKeyModel.controller_id)
        .filter(ControllerModel.uuid != controller.uuid)
        .filter(APIKeyModel.key == api_key)
        .first()
    )

    db.close()

    if registered_controller:
        raise HTTPException(
            **BACKEND_CONTROLLER_RESPONSES["REG_SUCCESS_CONTROLLERKNOWN"]
        )

    if claimed_api_keys:
        raise HTTPException(**BACKEND_CONTROLLER_RESPONSES["REG_ERROR_WRONG_CONFIG"])

    if not uuid_exists:
        registration_date = datetime.now()
        new_controller = ControllerModel(
            registration_date=registration_date, **controller.dict()
        )
        db = SessionLocal()
        unclaimed_api_key_instance = (
            db.query(APIKeyModel)
            .filter(not_(APIKeyModel.revoked))
            .filter(APIKeyModel.key == api_key)
            .first()
        )
        db.add(new_controller)
        db.commit()
        db.refresh(new_controller)
        unclaimed_api_key_instance.controller_id = new_controller.id
        db.commit()

        # create grafana dashboard
        grafana = GrafanaService()
        response = grafana.setup_controller(controller.uuid)
        logger.debug(response)
        if not response:
            raise HTTPException(status_code=500, detail="Internal Server Error")
        # response = grafana.create_folder(controller.uuid)
        # response = grafana.create_dashboard(controller.uuid)
        new_dashboard = DashboardModel(
            controller_id=new_controller.id,
            uid=response.uid,
            link=response.link,
        )
        db.add(new_dashboard)
        db.commit()
        db.refresh(new_dashboard)
        db.close()

        raise HTTPException(**BACKEND_CONTROLLER_RESPONSES["REG_SUCCESS"])

    raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/{controller}/register_device", tags=["controllers"])
async def register_device(
    controller: str,
    device: DeviceRegistration,
    api_key: APIKey = Depends(get_api_key),
):
    db = SessionLocal()

    registered_controller = (
        db.query(APIKeyModel)
        .join(ControllerModel, ControllerModel.id == APIKeyModel.controller_id)
        .filter(ControllerModel.uuid == controller)
        .filter(APIKeyModel.key == api_key)
        .first()
    )
    db.close()
    if not registered_controller:
        raise HTTPException(**BACKEND_CONTROLLER_RESPONSES["REG_ERROR_WRONG_CONFIG"])

    # check if device is already registered and if metadata matches
    db = SessionLocal()
    registered_device = (
        db.query(DeviceModel).filter(DeviceModel.uuid == device.uuid).first()
    )
    db.close()

    if registered_device:
        if not devices_match(device, registered_device):
            raise HTTPException(**BACKEND_DEVICE_RESPONSES["REG_ERROR_DEVICECONFIG"])
        if registered_controller.controller_id != registered_device.controller_id:
            raise HTTPException(**BACKEND_DEVICE_RESPONSES["REG_ERROR_WRONGCONTROLLER"])
        raise (HTTPException(**BACKEND_DEVICE_RESPONSES["REG_SUCCESS_DEVICEKNOWN"]))

    registration_date = datetime.now()
    new_device = DeviceModel(registration_date=registration_date, **device.dict())
    db = SessionLocal()
    controller_instance = (
        db.query(ControllerModel).filter(ControllerModel.uuid == controller).first()
    )
    new_device.controller_id = controller_instance.id
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    db.close()

    metadata = MetaData()
    create_table_from_json(
        metadata, device.uuid, device.measurement_model, device.parameter_model
    )

    metadata.create_all(engine)

    db = SessionLocal()

    db.execute(text("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE"))
    db.execute(
        text(
            f"SELECT create_hypertable('{device.uuid}', "
            f"'timestamp', if_not_exists => TRUE)"
        )
    )
    db.commit()

    raise HTTPException(**BACKEND_DEVICE_RESPONSES["REG_SUCCESS"])


# WebSocket endpoint
@router.websocket("/{controller}/ws")
async def websocket_endpoint(
    controller: str,
    websocket: WebSocket,
    apikey: Optional[str] = Depends(get_api_key_ws),
    redis: aioredis = Depends(get_redis_pool),
):
    db = SessionLocal()
    registered_controller = (
        db.query(APIKeyModel)
        .join(ControllerModel, ControllerModel.id == APIKeyModel.controller_id)
        .filter(ControllerModel.uuid == controller)
        .filter(APIKeyModel.key == apikey)
        .first()
    )
    db.close()
    if not registered_controller:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    # Accept the WebSocket connection
    await websocket.accept()

    channel_name = f"rpc_channel:{controller}"

    pubsub = redis.pubsub()
    await pubsub.subscribe(channel_name)

    async def listen_to_redis():
        async for message in pubsub.listen():
            if message["type"] == "message":
                logger.debug(f"Message from subscription: {message}")
                await websocket.send_text(message["data"].decode("utf-8"))

    async def listen_to_websocket():
        while True:
            data = await websocket.receive_json()
            data["controller_uuid"] = controller
            logger.debug(f"Received data: {data}")

            try:
                await redis.xadd("server_ws_recv", {"value": json.dumps(data)})
            except Exception as e:
                logger.error(
                    f"Exception thrown when adding datapoint to redis streams: {e}"
                )

    # Run both listeners concurrently.
    # They'll run until the WebSocket is closed.
    await asyncio.gather(listen_to_redis(), listen_to_websocket())

    # Clean up Redis subscriptions when done
    await pubsub.unsubscribe(channel_name)
    pubsub.close()


@router.post("/", tags=["controllers"])
async def create_controller(
    controller: ControllerCreate, current_user: User = Depends(validate)
):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    new_uuid = str(uuid.uuid4())
    registration_date = datetime.now()
    new_controller = ControllerModel(
        uuid=new_uuid, registration_date=registration_date, **controller.dict()
    )
    db.add(new_controller)
    db.commit()
    db.refresh(new_controller)
    db.close()
    return new_controller


@router.get("/", tags=["controllers"])
async def read_controller(current_user: User = Depends(validate)):
    db = SessionLocal()
    if "authentik Admins" in current_user.groups:
        controllers = db.query(ControllerModel).all()
        db.close()
    else:
        uuids_without_suffix = [
            group.split("_")[0]
            for group in current_user.groups
            if group.endswith(("_read", "_write"))
        ]
        controllers = (
            db.query(ControllerModel)
            .filter(ControllerModel.uuid.in_(uuids_without_suffix))
            .all()
        )
    db.close()
    return controllers


@router.put("/{controller_id}", tags=["controllers"])
async def update_controller(
    controller_id: int,
    controller: ControllerUpdate,
    current_user: User = Depends(validate),
):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_controller = (
        db.query(ControllerModel).filter(ControllerModel.id == controller_id).first()
    )
    if not db_controller:
        db.close()
        raise HTTPException(status_code=404, detail="Controller not found")
    for key, value in controller.dict().items():
        setattr(db_controller, key, value)
    db.commit()
    db.close()
    return db_controller


@router.delete("/{controller_id}", tags=["controllers"])
async def delete_controller(controller_id: int, current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_controller = (
        db.query(ControllerModel).filter(ControllerModel.id == controller_id).first()
    )
    if not db_controller:
        db.close()
        raise HTTPException(status_code=404, detail="Controller not found")
    db.delete(db_controller)
    db.commit()
    db.close()
    return {"status": "success"}


@router.get("/metadata", tags=["controllers"])
async def get_metadata(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    form_elements_create = generate_metadata(ControllerCreate)
    form_elements_update = generate_metadata(ControllerUpdate)

    # Generate column info based on APIKey SQLAlchemy model's columns
    columns = [
        {
            "name": column.name,
            "label": column.name.upper(),
            "field": column.name,
            "align": "left",
            "sortable": True if column.primary_key else False,
        }
        for column in ControllerModel.__table__.columns
    ]

    return {
        "formElementsUpdate": form_elements_update,
        "formElementsCreate": form_elements_create,
        "columns": columns,
    }


@router.get("/{controller_uuid}/devices", tags=["controllers"])
async def read_devices(controller_uuid: str, current_user: User = Depends(validate)):
    db = SessionLocal()
    uuids_without_suffix = [
        group.split("_")[0]
        for group in current_user.groups
        if group.endswith(("_read", "_write"))
    ]
    if (
        "authentik Admins" in current_user.groups
        or controller_uuid in uuids_without_suffix
    ):
        devices = (
            db.query(DeviceModel)
            .join(ControllerModel, DeviceModel.controller_id == ControllerModel.id)
            .filter(ControllerModel.uuid == controller_uuid)
            .all()
        )
        db.close()
    else:
        devices = []
    db.close()
    return devices


@router.get("/{controller_uuid}/dashboard", tags=["controller"])
async def read_dashboard(controller_uuid: str, current_user: User = Depends(validate)):
    db = SessionLocal()
    uuids_without_suffix = [
        group.split("_")[0]
        for group in current_user.groups
        if group.endswith(("_read", "_write"))
    ]
    # controller_uuid = (
    #     db.query(ControllerModel)
    #     .join(DeviceModel, DeviceModel.controller_id == ControllerModel.id)
    #     .filter(DeviceModel.uuid == controller_uuid)
    #     .first()
    # )
    db.close()
    if (
        "authentik Admins" in current_user.groups
        or controller_uuid in uuids_without_suffix
    ):
        db = SessionLocal()
        dashboard = (
            db.query(DashboardModel)
            .join(ControllerModel, DashboardModel.controller_id == ControllerModel.id)
            .filter(ControllerModel.uuid == controller_uuid)
            .first()
        )
        db.close()
    else:
        dashboard = []

    return dashboard


async def background_processing_task(
    task_id: str, start_date: str, end_date: str, uuids: str
):
    memory_file = io.BytesIO()

    try:
        redis = get_redis_pool()

        # Convert comma-separated uuids to a list
        uuid_list = uuids.split(",")

        inspector = inspect(engine)

        with zipfile.ZipFile(memory_file, "w", zipfile.ZIP_DEFLATED) as zf:
            for device_uuid in uuid_list:
                if not is_valid_uuid(device_uuid):
                    raise ValueError("Invalid UUID")

                # Dynamically get column names except for 'timestamp'
                # TODO: why did i do this again?

                columns = inspector.get_columns(device_uuid)
                column_names = [
                    col["name"] for col in columns if col["name"] != "timestamp"
                ]

                # Using raw SQL
                query = text(
                    f"""
                    SELECT timestamp, {', '.join(column_names)}
                    FROM "{device_uuid}"
                    WHERE timestamp BETWEEN :start_date AND :end_date
                    ORDER BY timestamp ASC
                """
                )
                result = engine.execute(query, start_date=start_date, end_date=end_date)

                csv_content = io.StringIO()
                writer = csv.writer(csv_content)

                # Write the header
                column_names.insert(0, "timestamp")
                writer.writerow(column_names)
                # Write the data
                for row in result:
                    writer.writerow(row)

                zf.writestr(f"{device_uuid}.csv", csv_content.getvalue())

        # Set the memory file pointer to the beginning
        memory_file.seek(0)

        # Store the ZIP file content and update the task status in Redis
        await redis.set(f"task_{task_id}_file", memory_file.getvalue())
        await redis.set(f"task_{task_id}", "completed")
        await redis.expire(f"task_{task_id}_file", 600)
        await redis.expire(f"task_{task_id}", 600)

        memory_file.close()

    except Exception as e:
        logger.error(f"Error in task {task_id}: {e}")
        # Set error status in Redis
        await redis.set(f"task_{task_id}", "error")

    finally:
        memory_file.close()


@router.get("/{controller_uuid}/devices/data/", tags=["controller"])
async def get_device_data(
    background_tasks: BackgroundTasks,
    controller_uuid: str,
    start_date: str,
    end_date: str,
    uuids: str,
    current_user: User = Depends(validate),
    redis: aioredis = Depends(get_redis_pool),
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
        return None

    # Starting a background task, since fetching the data from postgres can
    # easily exceed 60s timeout
    task_id = str(uuid4())
    await redis.set(f"task_{task_id}", "processing")
    background_tasks.add_task(
        background_processing_task,
        task_id,
        start_date,
        end_date,
        uuids,
    )

    return {"task_id": task_id}


@router.get("/tasks/{task_id}/status", tags=["controller"])
async def get_task_status(
    task_id: str,
    current_user: User = Depends(validate),
    redis: aioredis = Depends(get_redis_pool),
):
    status = await redis.get(f"task_{task_id}")
    if not status:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task_id": task_id, "status": status.decode("utf-8")}


@router.get("/tasks/{task_id}/download", tags=["controller"])
async def download_task_result(
    task_id: str,
    current_user: User = Depends(validate),
    redis: aioredis = Depends(get_redis_pool),
):
    status = await redis.get(f"task_{task_id}")
    if not status or status.decode("utf-8") != "completed":
        raise HTTPException(status_code=404, detail="Task not ready or not found")

    zip_content = await redis.get(f"task_{task_id}_file")
    if not zip_content:
        raise HTTPException(status_code=404, detail="File not found")

    response = StreamingResponse(
        iter([zip_content]), media_type="application/x-zip-compressed"
    )
    response.headers["Content-Disposition"] = "attachment; filename=bioterm_data.zip"
    response.headers["Content-Length"] = str(len(zip_content))

    await redis.delete(f"task_{task_id}")
    await redis.delete(f"task_{task_id}_file")

    return response
