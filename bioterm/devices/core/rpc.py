import inspect
from dataclasses import asdict

from ...common.core.logger import get_module_logger
from ...common.models.rpc.base_models import RPCPayload

logger = get_module_logger(__name__)


class RemoteProcedureCaller:
    def __init__(self, device):
        self.device = device
        self.rpc_methods = {}

    def to_json(self):
        json_rpc_methods = {}
        for method_name, input_objects in self.rpc_methods.items():
            json_rpc_methods[method_name] = []
            for obj in input_objects:
                # Convert the dataclass object to a dictionary
                obj_dict = asdict(obj)

                # Handle return_type specially, converting it to a string
                obj_dict["return_type"] = str(obj_dict["return_type"])

                # Append the object dictionary to the list
                json_rpc_methods[method_name].append(obj_dict)

        return json_rpc_methods
        # return json.dumps(json_rpc_methods, indent=4)

    def register_rpc(self, method, *input_objects):
        """
        Registers a remote procedure by associating it with input objects that define
         the UI elements for its arguments.

        :param method: The method to be registered as a remote procedure. It must be a
         callable object.
        :type method: callable
        :param input_objects: Variable-length argument list of input objects (UIElement
         or its subclasses) corresponding to the parameters of the method.
        :type input_objects: IntegerInput, FloatInput, TextInput, EnumInput, etc.

        :raises Exception: If the number of input objects provided does not match the
         number of arguments for the method.
        """
        method_name = method.__name__
        signature = inspect.signature(method)
        if len(signature.parameters) != len(input_objects):
            raise Exception(
                f"Number of input objects provided does not match the number of "
                f"arguments for method '{method_name}'."
            )

        self.rpc_methods[method_name] = input_objects

    def call_rpc(self, rpc: RPCPayload):
        """
        Calls a method on the Device object that has been registered as a remote
        procedure.

        :param json_request: JSON string containing the name of the method to
         call and its arguments.
        :type json_request: str
        :raises KeyError: If the method name is not found in the registered
         remote procedures.
        :raises TypeError: If the arguments do not match the expected types.
        """

        method_name = rpc.key
        args = rpc.params

        method = getattr(self.device, method_name, None)

        if method and callable(method) and method_name in self.rpc_methods:
            # Check if types of incoming arguments match the registered input objects
            input_objects = self.rpc_methods[method_name]
            expected_args = [obj.return_type for obj in input_objects]
            actual_args = [type(arg) for arg in args.values()]

            if expected_args != actual_args:
                return (
                    f"Error: Type mismatch for method {method_name}."
                    f"Expected {expected_args}, received {actual_args}."
                )

            # Call the method with the provided arguments
            return method(*args.values())
        else:
            return (
                f"Error: Method {method_name} not found or not registered as a remote "
                f"procedure call."
            )
