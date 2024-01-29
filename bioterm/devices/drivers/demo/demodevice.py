import json
import os
import queue
import random
import time
from datetime import datetime
from typing import Any
from typing import List

import pytz

from ....common.core.logger import get_module_logger
from ....common.models.control.base_models import Datapoint
from ...core.abstractDevice import AbstractDevice
from ...core.queues import DatapointQueue
from .models import EnumerableMeasurement
from .models import Measurement
from .models import Parameter

logger = get_module_logger(__name__)
utc_zone = pytz.timezone("UTC")


class demoDevice(AbstractDevice):
    synchronous_rpc_queue = queue.Queue()

    name: str
    data_list: List[Any]
    com_port: str
    baudrate: int

    def __init__(self, config_path):
        super().__init__(config_path)

        self.config_path = config_path

        # Read settings from the device's config.json file.
        try:
            self.name = self.config_data["myDeviceSettings"]["name"]
            self.data_list = self.config_data["myDeviceSettings"]["listOfData"]
            self.com_port = self.config_data["connectionSettings"]["com_port"]
            self.baudrate = self.config_data["connectionSettings"]["baudrate"]
        except KeyError:
            logger.fatal(
                "One or more properties are missing from the config file. "
                + "Writing template file with defaults to be filled out!"
            )

            # Generate a template config file so the user can transfer the missing keys
            # from the template file without losing the already existing one
            # in case the device has been updated with a new config file structure
            config_template = {
                "biotermDeviceSettings": self.config_data["biotermDeviceSettings"],
                "myDeviceSettings": {
                    "name": "",
                    "listOfData": [1, "two", "th", "re", "e"],
                },
                "connectionSettings": {"com_port": "", "baudrate": 115200},
            }

            path = os.path.join(os.path.dirname(config_path), "config_template.json")
            with open(path, "w") as f:
                json.dump(config_template, f, indent=4)

            exit(0)

        # Further initialization commands before the device starts running go here.
        # Sanity checks, setup routines etc.

        # Update settings file, need to write back into the dictionary
        self.config_data["myDeviceSettings"]["listOfData"] = self.data_list

        with open(config_path, "w") as f:
            json.dump(self.config_data, f, indent=4)

    def do_something_amazing(self, arg1: int, arg2: float, arg3: str):
        logger.info(f"I did a thing with {int(arg1)} and {float(arg2)} and {arg3}")

    # Registered RPCs will be called in the deviceManager's thread and not within
    # the device's actual thread. This means that races can occur when they are
    # accessing and manipulating shared data.
    # While some RPCs may not do that and can be called directly (do_something_amazing)
    # some other RPCs for example "do_something_regular", and "log_data_list" should
    # be executed synchronously within the device's thread, ESPECIALLY if the device
    # loop accesses these shared ressources aswell.
    # The way to handle this is to simply queue up the actual function implementation
    # and work through their Queue in the main loop. This is safe because
    # the implementation from Queue is threadsafe.

    def rotate_data_list(self):
        self.synchronous_rpc_queue.put([self.rotate_data_list_run, []])

    def rotate_data_list_run(self):
        self.data_list = self.data_list[1:] + self.data_list[0:1]

        # Write modified list back to config file.
        self.config_data["myDeviceSettings"]["listOfData"] = self.data_list
        with open(self.config_path, "w") as f:
            json.dump(self.config_data, f, indent=4)

    def log_data_list(self):
        # Pass 5 as an example parameter to the actual implementation.
        # You can also just relay the parameters from this RPC to the
        # actual implementation if the RPC has parameters.
        self.synchronous_rpc_queue.put([self.log_data_list_run, [5]])

    def log_data_list_run(self, max_log_count: int):
        datalist = ", ".join([str(x) for x in self.data_list[0:max_log_count]])
        logger.info(f"listOfData = [{datalist}]")
        return self.data_list

    def looped_device_interaction(
        self,
        task_queue: queue.Queue,
        return_queue: queue.Queue,
        datapoint_queue: DatapointQueue,
    ):
        # Work through all the queued up RPCs that should be executed synchronously
        while not self.synchronous_rpc_queue.empty():
            rpc_call = self.synchronous_rpc_queue.get()
            return_value = rpc_call[0](*rpc_call[1])

            # Do something with the return value if it's interesting.
            if return_value is not None:
                logger.info(
                    'RPC "'
                    + str(rpc_call[0].__name__)
                    + '" returned: '
                    + str(return_value)
                )

        # generate datapoint with random values
        random_int = random.randint(0, 100)
        random_float = round(random.uniform(0.0, 42.0), 2)
        random_enum = random.choice(list(EnumerableMeasurement))

        measurement = Measurement(
            int_value=random_int,
            float_value=random_float,
            enum_value=random_enum,
        )

        parameter = Parameter(gain=100, sampling_rate=1, sensitivity="1")

        datapoint = Datapoint(
            timestamp=datetime.now(utc_zone),
            meas=measurement.dict(),
            param=parameter.dict(),
        )

        datapoint_queue.put(datapoint)
        logger.debug(datapoint)

        time.sleep(1)
