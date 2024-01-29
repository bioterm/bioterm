from enum import Enum

from pydantic import Field

from ....common.models.control.base_models import AbstractMeasurement


class EnumerableParameter(str, Enum):
    LOW_SENSITIVITY = "1"
    HIGH_SENSITIVITY = "2"


class EnumerableMeasurement(str, Enum):
    OVERFULL = "overfull"
    FULL = "full"
    LOW = "low"
    EMPTY = "empty"


class Parameter(AbstractMeasurement):
    sampling_rate: int = Field(..., ge=0, le=100, read_only=True)
    sensitivity: EnumerableParameter
    gain: int = Field(..., ge=0, le=100)


class Measurement(AbstractMeasurement):  #
    int_value: int = Field(..., ge=0, le=100)  # A value between 0 and 100
    float_value: float = Field(..., ge=0.0, le=42.0)  # A value between 0.0 and 42.0
    enum_value: EnumerableMeasurement
