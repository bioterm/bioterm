import asyncio
import datetime
import json
import socket

from redis import asyncio as aioredis
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from ....common.core.logger import get_module_logger
from ....common.models.apikeys.database_models import APIKeyModel  # noqa: F401
from ....common.models.controllers.database_models import ControllerModel  # noqa: F401
from ....common.models.devices.database_models import DeviceModel
from ....common.models.grafana.database_models import DashboardModel  # noqa: F401
from ....common.models.grafana.database_models import PanelModel  # noqa: F401
from ....common.models.rules.database_models import RuleModel  # noqa: F401
from ..core.config import POSTGRES_DB
from ..core.config import POSTGRES_PASSWORD
from ..core.config import POSTGRES_SERVER
from ..core.config import POSTGRES_USER
from ..core.config import REDIS_URL


logger = get_module_logger(__name__)


SQLALCHEMY_DATABASE_URI = (
    f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_SERVER}/{POSTGRES_DB}"
)

# Mapping for JSON types to SQLAlchemy types
TYPE_MAPPING = {
    "string": String,
    "integer": Integer,
    "number": Float,
    "boolean": String,
}

engine = create_async_engine(SQLALCHEMY_DATABASE_URI, echo=False)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
metadata = MetaData()

json_schema_cache = {}


# async def reflect_metadata():
#     async with engine.begin() as conn:
#         await conn.run_sync(metadata.reflect)


async def reflect_specific_metadata(table_name):
    """
    Reflects the metadata of a specific table from the database.

    This function attempts to reflect the schema of the specified table. If the table
    doesn't exist or an error occurs during reflection, it logs a warning.

    :param table_name: The name of the table to reflect.
    :type table_name: str
    :return: A boolean indicating whether the reflection was successful.
    :rtype: bool
    """
    async with engine.begin() as conn:
        try:
            await conn.run_sync(metadata.reflect, only=[table_name])
        except InvalidRequestError:
            logger.warning(f"Failed to reflect table: {table_name}")
            return False
    return True


def validate_data_against_schema(data, json_schema):
    """
    Validates a dictionary of data against a provided JSON schema.

    This function checks if the provided data adheres to the structure and data types
    defined in the JSON schema. It raises a ValueError with a descriptive message if
    the validation fails.

    :param data: The data to validate.
    :type data: dict
    :param json_schema: The JSON schema to validate against.
    :type json_schema: dict
    :raises ValueError: If the data does not conform to the schema.
    """
    properties = json_schema["properties"]
    errors = []

    for prop, details in properties.items():
        if prop not in data:
            errors.append(f"Missing property: {prop}")
            continue

        value = data[prop]

        if prop == "timestamp":
            if not isinstance(value, datetime.datetime):
                errors.append(
                    f"Invalid type for {prop}. "
                    f"Expected datetime, got {type(value).__name__}."
                )
            continue

        if "$ref" in details:  # Handle referenced enum type
            enum_name = details["$ref"].split("/")[-1]
            enum_values = json_schema["$defs"][enum_name]["enum"]

            if value not in enum_values:
                errors.append(
                    f"Invalid value for {prop}. "
                    f"Expected one of {enum_values}, got {value}."
                )
        else:
            # # Type validation, currently disabled for performance increase
            # type_name = details["type"]
            # if type_name == "string" and not isinstance(value, str):
            #     errors.append(
            #         f"Invalid type for {prop}. "
            #         f"Expected string, got {type(value).__name__}."
            #     )
            # elif type_name == "number" and not isinstance(value, (int, float)):
            #     errors.append(
            #         f"Invalid type for {prop}. "
            #         f"Expected number, got {type(value).__name__}."
            #     )
            # elif type_name == "integer" and not isinstance(value, int):
            #     errors.append(
            #         f"Invalid type for {prop}. "
            #         f"Expected integer, got {type(value).__name__}."
            #     )
            # elif type_name == "boolean" and not isinstance(value, bool):
            #     errors.append(
            #         f"Invalid type for {prop}. "
            #         f"Expected boolean, got {type(value).__name__}."
            #     )

            # Additional constraints
            if "minimum" in details and value < details["minimum"]:
                errors.append(
                    f"Value for {prop} is below the minimum of {details['minimum']}."
                )
            if "maximum" in details and value > details["maximum"]:
                errors.append(
                    f"Value for {prop} is above the maximum of {details['maximum']}."
                )
            if "minLength" in details and len(value) < details["minLength"]:
                errors.append(
                    f"Length of {prop} is below the minimum length "
                    f"of {details['minLength']}."
                )
            if "maxLength" in details and len(value) > details["maxLength"]:
                errors.append(
                    f"Length of {prop} is above the maximum length "
                    f"of {details['maxLength']}."
                )

    if errors:
        raise ValueError("; ".join(errors))


async def insert_data_into_table(session, table, data):
    """
    Asynchronously inserts data into a specified table.

    This coroutine function inserts the given data into the specified table using the
    provided session.

    :param session: The database session to use for the insertion.
    :type session: AsyncSession
    :param table: The table object where data needs to be inserted.
    :type table: Table
    :param data: The data to be inserted into the table.
    :type data: dict
    """
    await session.execute(table.insert().values(**data))


async def fetch_json_schemas(session, table_uuid):
    """
    Asynchronously fetches JSON schemas for a given table UUID.

    This coroutine function retrieves measurement and parameter models as JSON schemas
    from the database for the specified UUID table.

    :param session: The database session to use for the query.
    :type session: AsyncSession
    :param table_uuid: The UUID of the table for which to fetch the schemas.
    :type table_uuid: str
    :return: A tuple containing the measurement model JSON schema and the parameter
             model JSON schema.
    :rtype: tuple or None
    """
    stmt = select(DeviceModel.measurement_model, DeviceModel.parameter_model).where(
        DeviceModel.uuid == table_uuid
    )
    result = await session.execute(stmt)
    device_record = result.fetchone()

    if device_record:
        return device_record.measurement_model, device_record.parameter_model
    return None


async def process_message(session, message):
    """
    Asynchronously processes a single message.

    This coroutine processes a message, validates its data against JSON schemas, and
    inserts it into the database. If schemas are not found or the message format is
    incorrect, it logs a warning.

    :param session: The database session to use for data insertion and schema fetching.
    :type session: AsyncSession
    :param message: The message to process.
    :type message: dict
    :raises Exception: If message processing fails for any reason.
    """
    try:
        raw_value = message[b"value"].decode("utf-8")
        value = json.loads(raw_value)

        uuid_table = value["data"]["uuid"].lower()

        # Handles tables created while this process is already running
        if uuid_table not in dict(metadata.tables):
            logger.debug(f"Reflecting metadata for table: {uuid_table}")
            success = await reflect_specific_metadata(uuid_table)
            if not success or uuid_table not in dict(metadata.tables):
                logger.warning(f"No table defined for UUID: {uuid_table}")
                return

        if uuid_table in json_schema_cache:
            meas_json_schema, param_json_schema = json_schema_cache[uuid_table]
        else:
            logger.debug(f"Fetching JSON schema for table: {uuid_table}")
            schema_result = await fetch_json_schemas(session, uuid_table)
            if schema_result:
                meas_json_schema, param_json_schema = schema_result
                json_schema_cache[uuid_table] = (meas_json_schema, param_json_schema)
            else:
                logger.warning(f"No schema found for table: {uuid_table}")
                return  # Skip processing if no schema found

        table = metadata.tables[uuid_table]

        data_to_insert = json.loads(value["data"]["value"])
        logger.debug(f"data_to_insert: {data_to_insert}")

        # Convert timestamp if present
        if "timestamp" in data_to_insert:
            data_to_insert["timestamp"] = datetime.datetime.fromisoformat(
                data_to_insert["timestamp"]
            ).replace(tzinfo=datetime.timezone.utc)

        # Validate 'meas' and 'param' separately, if they are not None
        meas_data = data_to_insert.get("meas")
        if meas_data is not None:
            validate_data_against_schema(meas_data, meas_json_schema)

        param_data = data_to_insert.get("param")
        if param_data is not None:
            validate_data_against_schema(param_data, param_json_schema)

        # Flatten and prefix the 'meas' and 'param' data for insertion
        flattened_data = {"timestamp": data_to_insert["timestamp"]}
        if meas_data:
            for key, value in meas_data.items():
                flattened_data[f"meas_{key}"] = value

        if param_data:
            for key, value in param_data.items():
                flattened_data[f"prop_{key}"] = value

        # Only insert if data keys match table columns
        column_names = [col.name for col in table.columns]

        if set(flattened_data.keys()) == set(column_names):
            await insert_data_into_table(session, table, flattened_data)
        else:
            logger.warning(
                f"Data keys do not match for table '{uuid_table}': "
                f"{flattened_data.keys()}"
            )
            return

    except Exception as e:
        logger.error(f"Failed to process message: {e}")


async def main():
    """
    The main coroutine function of the script.

    This function sets up a Redis connection, creates a consumer group, and continuously
    reads and processes messages from a Redis stream. It handles message acknowledgments
    and maintains a database session for operations.
    """
    redis = await aioredis.from_url(REDIS_URL)

    consumer_id = socket.gethostname()

    # Create a consumer group if it doesn't exist
    try:
        await redis.xgroup_create("server_ws_recv", "dbworker", id="0", mkstream=True)
    except aioredis.ResponseError as e:
        # Ignore error if the group already exists
        if "BUSYGROUP Consumer Group name already exists" not in str(e):
            raise

    async with AsyncSessionLocal() as session:
        while True:
            messages = await redis.xreadgroup(
                "dbworker", consumer_id, {"server_ws_recv": ">"}, count=100, block=100
            )

            message_ids = []
            processing_tasks = []

            for _, message_list in messages:
                for message_id, message_data in message_list:
                    # Create a coroutine for each message and add it to the list
                    task = process_message(session, message_data)
                    processing_tasks.append(task)
                    message_ids.append(message_id)

            # Process all messages concurrently
            if processing_tasks:
                await asyncio.gather(*processing_tasks)

            await session.commit()

            if message_ids:
                # Acknowledge all the messages at once in the Redis stream
                await redis.xack("server_ws_recv", "dbworker", *message_ids)


if __name__ == "__main__":
    asyncio.run(main())
