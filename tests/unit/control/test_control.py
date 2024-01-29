import pytest

from ....bioterm.common.control.conditions import evaluate_condition
from ....bioterm.common.models.control.base_models import AllDevicesLastStatus
from ....bioterm.common.models.control.base_models import DeviceLastStatus
from ....bioterm.common.models.rules.base_models import LogicCondition
from ....bioterm.common.models.rules.base_models import ValueCondition

# from ....bioterm.common.models.control.base_models import MeasurementValue

# from ....bioterm.common.models.control.base_models import TimeCondition


# Fixture for device statuses
@pytest.fixture
def device_statuses() -> AllDevicesLastStatus:
    return AllDevicesLastStatus(
        devices={
            "Thermostat": DeviceLastStatus(
                name="Thermostat",
                timestamp="2023-11-10T00:28:44.510601",
                last_id="1-0",
                meas={"Temperature": 72},
            ),
            "Pump": DeviceLastStatus(
                name="Pump",
                timestamp="2023-11-10T00:28:45.332611",
                last_id="2-0",
                meas={"IsOn": True},
            ),
        }
    )


def test_evaluate_value_condition_equal(device_statuses):
    # Testing ValueCondition
    value_condition = ValueCondition(
        device="Thermostat", meas="Temperature", operator="eq", value=72
    )
    assert evaluate_condition(value_condition, device_statuses)


def test_evaluate_value_condition_notequal(device_statuses):
    # Testing ValueCondition
    value_condition = ValueCondition(
        device="Thermostat", meas="Temperature", operator="neq", value=72
    )
    assert not evaluate_condition(value_condition, device_statuses)


def test_evaluate_value_condition_lessequal(device_statuses):
    # Testing ValueCondition
    value_condition = ValueCondition(
        device="Thermostat", meas="Temperature", operator="leq", value=73
    )
    assert evaluate_condition(value_condition, device_statuses)


def test_evaluate_value_condition_greaterequal(device_statuses):
    # Testing ValueCondition
    value_condition = ValueCondition(
        device="Thermostat", meas="Temperature", operator="geq", value=71
    )
    assert evaluate_condition(value_condition, device_statuses)


def test_evaluate_value_condition_less(device_statuses):
    # Testing ValueCondition
    value_condition = ValueCondition(
        device="Thermostat", meas="Temperature", operator="le", value=74
    )
    assert evaluate_condition(value_condition, device_statuses)


def test_evaluate_value_condition_greater(device_statuses):
    # Testing ValueCondition
    value_condition = ValueCondition(
        device="Thermostat", meas="Temperature", operator="ge", value=72
    )
    assert not evaluate_condition(value_condition, device_statuses)


def test_evaluate_logic_condition_and(device_statuses):
    # Testing LogicCondition with AND operator
    sub_conditions = [
        ValueCondition(
            device="Thermostat", meas="Temperature", operator="geq", value=70
        ),
        ValueCondition(device="Pump", meas="IsOn", operator="eq", value=True),
    ]
    logic_condition = LogicCondition(operator="AND", conditions=sub_conditions)
    assert evaluate_condition(logic_condition, device_statuses)


def test_evaluate_logic_condition_or(device_statuses):
    # Testing LogicCondition with OR operator
    sub_conditions = [
        ValueCondition(
            device="Thermostat", meas="Temperature", operator="le", value=65
        ),
        ValueCondition(device="Pump", meas="IsOn", operator="eq", value=True),
    ]
    logic_condition = LogicCondition(operator="OR", conditions=sub_conditions)
    assert evaluate_condition(logic_condition, device_statuses)


def test_unrecognized_condition_type(device_statuses):
    # Testing with an unrecognized condition type
    unrecognized_condition = "This is not a condition object"
    assert not evaluate_condition(unrecognized_condition, device_statuses)
