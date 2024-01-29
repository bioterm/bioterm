import dataclasses
import json
import queue
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Type

import aioprocessing
from pydantic import BaseModel

from ...common.core.logger import get_module_logger
from ...common.core.responses import BACKEND_DEVICE_RESPONSES
from ...common.models.devices.base_models import DeviceRegistration
from .abstractDevice import AbstractDevice
from .ipc import IPC
from .queues import DatapointQueue
from .rpc import RemoteProcedureCaller

logger = get_module_logger(__name__)


class ProtoDeviceManager:
    def __init__(self, device: AbstractDevice):
        self.device = device
        self.rpc_caller = RemoteProcedureCaller(device)
        self.ipc = IPC()
        self.queue = aioprocessing.AioQueue()
        self.measurement_model = None
        self.parameter_model = None
        self.parameter_model = None
        self.queue_timeout = 0.1

    def register_remote_procedure(self, method_name, *input_objects):
        return self.rpc_caller.register_rpc(method_name, *input_objects)

    def call_remote_procedure(self, json_request):
        return self.rpc_caller.call_rpc(json_request)

    def register_parameter_model(self, model: Type[BaseModel]):
        self.parameter_model = model

    def register_measurement_model(self, model: Type[BaseModel]):
        self.measurement_model = model

    def _register_device(self):
        if self.measurement_model is None:
            logger.error("Missing measurement model!")
            sys.exit(1)

        if self.parameter_model is None:
            logger.error("Missing parameter model!")
            sys.exit(1)

        # Wait until the registration service is ready:
        while True:
            if self.ipc.redis_conn.get("registration_service_status") == b"READY":
                break
            time.sleep(5)  # Check every 5 seconds.

        # Create a dedicated channel for this device's response:
        response_channel = f"response_{self.device.uuid}"
        if self.ipc.channel_exists(response_channel):
            logger.error("Device UUID not unique")
            sys.exit(1)

        pubsub = self.ipc.redis_conn.pubsub()
        pubsub.subscribe(response_channel)

        # Create device descriptor json
        deviceDescriptor = DeviceRegistration(
            uuid=self.device.uuid,
            display_name="",
            parameters={"hello": "world"},
            measurement_model=self.measurement_model.schema(),
            parameter_model=self.parameter_model.schema(),
            rpc=self.rpc_caller.to_json(),
        )
        logger.info(deviceDescriptor.json())

        # Send registration to the "device_registration" channel
        self.ipc.redis_conn.publish("device_registrations", deviceDescriptor.json())

        for message in pubsub.listen():
            if message["type"] == "message":
                # Decode and parse the message data.
                message_data_str = message["data"].decode()
                message_data = json.loads(message_data_str)

                # Extract status code and details.
                status_code = message_data.get("status_code")
                detail_data = json.loads(message_data.get("text"))
                detail = detail_data.get("detail")

                handled = False  # Flag to check if the response was handled

                for key, value in BACKEND_DEVICE_RESPONSES.items():
                    if (
                        status_code == value["status_code"]
                        and detail == value["detail"]
                    ):
                        if "SUCCESS" in key:
                            logger.debug(value["detail"])
                            handled = True
                            break
                        else:
                            logger.error(value["detail"])
                            handled = True
                            sys.exit(1)

                # Log an error for unexpected responses.
                if not handled:
                    logger.error(f"Unexpected response: {status_code} - {detail}")
                    sys.exit(1)
                else:
                    break

        # # Wait for up to 5 seconds for a confirmation message
        # confirmation = pubsub.get_message(timeout=5)
        # if confirmation and json.loads(confirmation["data"])["name"] == self.name:
        #     print(f"Consumer {self.name} registered successfully.")
        # else:
        #     print(f"Registration failed for consumer {self.name}.")

    async def print_queue(self):
        while True:
            message = await self.queue.coro_get()  # Read from the queue
            json_str = json.dumps(dataclasses.asdict(message))
            self.ipc.send_to_stream(json_str)

    def run_device(self, stream_name):
        self._register_device()

        logger.info("Starting device...")

        task_queue = queue.Queue()
        return_queue = queue.Queue()
        datapoint_queue = DatapointQueue()

        # Run everything in separate threads
        with ThreadPoolExecutor() as executor:
            # future_device_run = executor.submit(
            #     self.device.run, task_queue, return_queue, datapoint_queue
            # )

            # Submitting listen_to_stream to the thread pool
            executor.submit(
                self.ipc.listen_to_stream,
                self.device.uuid,
                task_queue,
                return_queue,
                self.call_remote_procedure,
            )

            # Submitting send_to_stream to the thread pool
            executor.submit(
                self.ipc.send_to_stream,
                "telemetrystream",
                datapoint_queue,
                self.queue_timeout,
                self.device.uuid,
            )

            # # Start listening to IPC
            # self.ipc.listen_to_stream(
            #     "test", task_queue, return_queue, self.call_remote_procedure
            # )

            self.device.run(task_queue, return_queue, datapoint_queue)

            # Add stop condition to the queue to exit the threads
            task_queue.put(None)
            return_queue.put(None)
            datapoint_queue.put(None)

        # Ensure Device.run has completed
        # device_run_result = future_device_run.result()
        # listen_result = future_listen.result()
        # send_result = future_send.result()


# def run_device(self, stream_name):
#     # Create a Process to run the device's run method, passing the queue
#     device_process = multiprocessing.Process(
#         target=self.device.run, args=(self.queue,)
#     )

#     # Start the process
#     device_process.start()

#     # Create an asyncio loop to run both IPC and queue printing
#     loop = asyncio.get_event_loop()

#     # Run the IPC listener
#     ipc_task = loop.run_in_executor(
#         None, self.ipc.listen_to_stream, stream_name, self.call_remote_procedure
#     )

#     # Run the queue print loop
#     print_queue_task = asyncio.ensure_future(self.print_queue())

#     # Run both tasks
#     loop.run_until_complete(asyncio.gather(ipc_task, print_queue_task))

#     # Wait for the device process to finish
#     device_process.join()

# # You can add additional DeviceManager methods here as needed

# # def run_device(self, stream_name):
# #     """Starts listening for incoming messages in a
# #        Redis stream and executes remote procedure calls.

# #     :param stream_name: Name of the Redis stream to listen to
# #     """
# #     # Create a Redis connection

# #     # The last message read
# #     last_id = "0"

# #     # Listen for messages indefinitely
# #     while True:
# #         # Read new messages from the stream
# #         messages = redis_conn.xread({stream_name: last_id}, count=1, block=0)

# #         for _, message_list in messages:
# #             for message in message_list:
# #                 message_id, content = message
# #                 json_request = content.get(b"message").decode("utf-8")

# #                 # Call the remote procedure specified in the message
# #                 result = self.call_remote_procedure(json_request)

# #                 # You could do something with the result here
# #                 print(result)

# #                 # Update the last message read
# #                 last_id = message_id
