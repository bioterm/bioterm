import asyncio
import json
import sys

import httpx
import requests

from ...common.core.config import getenv_boolean
from ...common.core.logger import get_module_logger
from ...common.core.responses import BACKEND_CONTROLLER_RESPONSES
from ...common.core.responses import BACKEND_DEVICE_RESPONSES
from ..core.config import API_DOMAIN
from ..core.config import CONTROLLER_APIKEY
from ..core.config import CONTROLLER_UUID
from ..core.redis_connector import get_redis_connection

logger = get_module_logger(__name__)

message_queue = asyncio.Queue()

CONTROLLER_REGISTRATION_URL = (
    f"https://{API_DOMAIN}/api/v0/controller/register_controller"
)
DEVICE_REGISTRATION_URL = (
    f"https://{API_DOMAIN}/api/v0/controller/{CONTROLLER_UUID}/register_device"
)
SERVICE_STATUS_KEY = "registration_service_status"
TTL_SECONDS = 10
headers = {"access-token": CONTROLLER_APIKEY}


async def run_sync(func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, lambda: func(*args, **kwargs))
    return result


async def async_send_to_api_endpoint(raw_json: str):
    logger.debug(raw_json)
    async with httpx.AsyncClient(verify=getenv_boolean("USE_TLS")) as client:
        response = await client.post(
            DEVICE_REGISTRATION_URL,
            json=json.loads(raw_json),
            headers=headers,
        )
        logger.debug(response)
    return response


async def refresh_service_status_key():
    r = get_redis_connection()
    while True:
        await run_sync(r.setex, SERVICE_STATUS_KEY, TTL_SECONDS, "READY")
        await asyncio.sleep(5)  # Refresh every 5 seconds


def handle_response(response_dict, response):
    response_data = response.json()
    detail = response_data.get("detail")
    for key, value in response_dict.items():
        if response.status_code == value["status_code"] and detail == value["detail"]:
            logger_method = logger.info if "SUCCESS" in key else logger.error
            logger_method(value["detail"])
            return 0 if "SUCCESS" in key else 1

    logger.error(f"Unexpected response: {response.status_code} - {detail}")
    return 1


def register_controller():
    data = {"uuid": CONTROLLER_UUID, "controller": "blubb"}
    return requests.post(
        CONTROLLER_REGISTRATION_URL,
        headers=headers,
        json=data,
        verify=getenv_boolean("USE_TLS"),
    )


def listen_for_messages(channel):
    for message in channel.listen():
        logger.debug(message)
        if message["type"] == "message":
            raw_json = message["data"].decode("utf-8")
            message_queue.put_nowait(raw_json)


def serialize_response(response):
    data = {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "text": response.text,
    }
    return json.dumps(data)


async def process_messages():
    r = get_redis_connection()
    while True:
        data = await message_queue.get()
        logger.debug(f"Processing data from queue: {data}")
        response = await async_send_to_api_endpoint(data)
        response_channel = f'response_{json.loads(data)["uuid"]}'
        result = handle_response(BACKEND_DEVICE_RESPONSES, response)
        if result == 0:
            logger.info(f'Registration of device {json.loads(data)["uuid"]} successful')
        #     await run_sync(r.publish, response_channel, "SUCCESS")
        else:
            logger.warning(f'Registration of device {json.loads(data)["uuid"]} failed')
        #     await run_sync(r.publish, response_channel, "FAILED")
        await run_sync(r.publish, response_channel, serialize_response(response))


async def registrationservice():
    response = register_controller()
    result = handle_response(BACKEND_CONTROLLER_RESPONSES, response)
    if result == 1:
        sys.exit(1)

    # Start the background task to refresh the service status key
    asyncio.create_task(refresh_service_status_key())

    r = get_redis_connection()
    pubsub = r.pubsub()
    pubsub.subscribe("device_registrations")

    # Run the subscriber function in a separate thread
    listener_task = asyncio.create_task(run_sync(listen_for_messages, pubsub))
    process_task = asyncio.create_task(process_messages())
    await process_task
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        # If this task is cancelled, make sure the listener task is closed
        listener_task.cancel()


logger.info("Starting registrationservice...")
loop = asyncio.get_event_loop()
loop.run_until_complete(registrationservice())
