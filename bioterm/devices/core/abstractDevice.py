import json
import os
import queue
import uuid
from abc import ABC
from abc import abstractmethod

from ...common.core.logger import get_module_logger
from ..core.queues import DatapointQueue

logger = get_module_logger(__name__)


class AbstractDevice(ABC):
    """
    Abstract base class for connected devices.
    """

    def __init__(self, config_path=None):
        self.logger = get_module_logger(__name__)
        self._uuid = None
        if not config_path:
            raise ValueError("Configuration path must be provided.")

        # Check if the provided path exists and is a valid JSON
        if not os.path.exists(config_path):
            raise ValueError(f"Configuration path {config_path} does not exist.")

        try:
            with open(config_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f"Configuration file {config_path} is not a valid JSON.")

        # Check for biotermDeviceSettings and uuid
        if "biotermDeviceSettings" not in data:
            data["biotermDeviceSettings"] = {"uuid": str(uuid.uuid4())}
        elif not data["biotermDeviceSettings"].get("uuid"):
            data["biotermDeviceSettings"]["uuid"] = str(uuid.uuid4())

        self._uuid = data["biotermDeviceSettings"]["uuid"]

        # Save the modified configuration back to file
        with open(config_path, "w") as f:
            json.dump(data, f, indent=4)

        self.config_data = data
        super().__init__()

    @property
    def uuid(self):
        """Getter for UUID."""
        return self._uuid

    @uuid.setter
    def uuid(self, new_uuid):
        """Setter for UUID. Usually, UUIDs shouldn't be modified once set,
        but if there's a valid use case, this setter can be utilized."""
        self._uuid = new_uuid
        self.logger.debug(f"Device UUID changed to: {self._uuid}")

    def run(
        self,
        task_queue: queue.Queue,
        return_queue: queue.Queue,
        datapoint_queue: DatapointQueue,
    ):
        while True:
            try:
                task = task_queue.get_nowait()  # Non-blocking get from the queue
                if task is None:  # Stop condition
                    break
                method_name, args = task["method"], task["args"]
                method = getattr(self, method_name)
                result = method(**args)
                logger.debug(f"{result}")

            # Handle the queue beeing empty
            except queue.Empty:
                logger.debug("Queue was empty...")

                # continue

            self.looped_device_interaction(task_queue, return_queue, datapoint_queue)

    @abstractmethod
    def looped_device_interaction(self, task_queue, return_queue, datapoint_queue):
        """
        Implement the specific behavior of the device here.
        This method will be called in the while True loop of run().
        Carefully consider that blocking code should be used to make use of threading.
        """
        pass
