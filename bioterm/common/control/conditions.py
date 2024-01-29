from ..core.logger import get_module_logger
from ..models.control.base_models import AllDevicesLastStatus
from ..models.rules.base_models import Condition
from ..models.rules.base_models import LogicCondition
from ..models.rules.base_models import ValueCondition

# from ..models.control.base_models import TimeCondition

logger = get_module_logger(__name__)


def evaluate_condition(
    condition: Condition,
    devices: AllDevicesLastStatus,
) -> bool:
    """
    Evaluates the condition based on its type and returns True or False.

    :param condition: A condition object of type LogicCondition, ValueCondition, or
                        TimeCondition.
    :param devices: An AllDevicesLastStatus object that stores the last measurement
                        value of all devices.
    :return: A boolean indicating the result of the condition evaluation.
    """
    # If it's a LogicCondition, recursively evaluate its nested conditions
    if isinstance(condition, LogicCondition):
        # If operator is AND, all conditions must be true
        if condition.operator == "AND":
            return all(
                evaluate_condition(sub_cond, devices)
                for sub_cond in condition.conditions
            )
        # If operator is OR, any condition being true is sufficient
        elif condition.operator == "OR":
            return any(
                evaluate_condition(sub_cond, devices)
                for sub_cond in condition.conditions
            )

    # If it's a ValueCondition, evaluate based on the operator and the value
    elif isinstance(condition, ValueCondition):
        # Fetch the last device measurement value
        # Returns False if the respective device has not (yet) recorded a value
        actual_value = None
        if condition.device in devices.devices:
            if condition.meas in devices.devices[condition.device].meas:
                actual_value = devices.devices[condition.device].meas[condition.meas]
        if actual_value is None:
            return False
        if condition.operator == "eq":
            return actual_value == condition.value
        if condition.operator == "le":
            return actual_value < condition.value
        if condition.operator == "leq":
            return actual_value <= condition.value
        if condition.operator == "ge":
            return actual_value > condition.value
        if condition.operator == "geq":
            return actual_value >= condition.value
        if condition.operator == "neq":
            return actual_value != condition.value

    # # If it's a TimeCondition, evaluate based on the current time
    # elif isinstance(condition, TimeCondition):
    #     # Fetch the current system time or use a timer to evaluate; for example:
    #     # current_time = get_current_time()
    #     current_time = ...  # Replace with actual time fetching logic
    #     return current_time >= condition.value

    # Return False if the condition is not recognized
    else:
        return False
