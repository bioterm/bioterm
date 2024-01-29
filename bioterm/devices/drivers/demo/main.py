from ....common.core.logger import get_module_logger
from ...core.deviceManager import ProtoDeviceManager
from ...core.uielements import FloatInput
from ...core.uielements import IntegerInput
from ...core.uielements import TextInput
from .demodevice import demoDevice
from .models import Measurement
from .models import Parameter

logger = get_module_logger(__name__)


def main(config_path):
    logger.info("Starting demo device driver...")
    myDevice = demoDevice(config_path)
    logger.debug(f"Running with configuration: {myDevice.config_data}")

    myDeviceManager = ProtoDeviceManager(myDevice)
    logger.debug("Registering Measurement...")
    myDeviceManager.register_measurement_model(Measurement)
    logger.debug("Registering Parameter...")
    myDeviceManager.register_parameter_model(Parameter)

    logger.debug("Registering RPCs...")
    myDeviceManager.register_remote_procedure(
        myDevice.do_something_amazing,
        IntegerInput(
            minValue=10,
            maxValue=20,
            increment=2,
            name="bla",
            id="blubb",
        ),
        FloatInput(
            minValue=10,
            maxValue=20,
            increment=2,
            name="blabla",
            id="blubb2",
        ),
        TextInput(
            regex=r"^\w+$",
            name="bla2",
            id="blubb3",
        ),
    )
    myDeviceManager.register_remote_procedure(
        myDevice.rotate_data_list,
    )
    myDeviceManager.register_remote_procedure(
        myDevice.log_data_list,
    )
    logger.debug(f"Serialized JSON of RPC: {myDeviceManager.rpc_caller.to_json()}")
    # myDeviceManager.print_rpc()

    # json_request = '{"method_name": "do_something_regular", "args": {}}'
    # logger.info(f"Testing RPC: {json_request}")
    # myDeviceManager.call_remote_procedure(json_request)
    # time.sleep(2)
    # json_request = (
    #     '{"method_name": "do_something_amazing", '
    #     '"args": {"arg1": 123, "arg2": "Hello, World!"}}'
    # )
    # logger.info(f"Testing RPC: {json_request}")
    # myDeviceManager.call_remote_procedure(json_request)
    # time.sleep(2)
    # # finally, we hand everything over to the device manager
    logger.debug("Handing over to device manager...")
    myDeviceManager.run_device("demo device")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        logger.error("Usage: python main_script.py <path_to_config>")
        sys.exit(1)

    config_path = sys.argv[1]
    main(config_path)
