from abc import ABC
from datetime import datetime
from typing import Any
from typing import Dict
from typing import get_type_hints
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import field_validator
from pydantic import model_validator

# from typing import List
# from typing import Literal
# from pydantic import Field

# from typing_extensions import Annotated


# class BaseCondition(BaseModel, ABC):
#     dwell: Optional[float] = None


# class LogicCondition(BaseCondition):
#     operator: Literal["AND", "OR"]
#     conditions: List["Condition"]  # union defined below


# class ValueCondition(BaseCondition):
#     device: str
#     meas: str
#     value: Union[str, int, float]
#     operator: Literal["eq", "le", "leq", "ge", "geq", "neq"]


# class TimeCondition(BaseCondition):
#     value: float
#     operator: Literal["time"] = "time"


# Condition = Annotated[
#     Union[LogicCondition, ValueCondition, TimeCondition],
#     Field(discriminator="operator"),
# ]


# class MeasurementValue(BaseModel, ABC):
#     value: Union[str, int, float]


def convert_datetime(dt: datetime) -> str:
    # always represent datetime with 6 digits for microseconds
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")


class DeviceLastStatus(BaseModel, ABC):
    timestamp: datetime
    last_id: str
    # meas: Dict[str, MeasurementValue]
    meas: Dict[str, Union[str, int, float]]

    # use custom json encoder
    class Config:
        json_encoders = {datetime: convert_datetime}


class AllDevicesLastStatus(BaseModel, ABC):
    devices: Dict[str, DeviceLastStatus]


# class Argument(BaseModel, ABC):
#     name: str
#     value: Union[str, int, float]


# class Method(BaseModel, ABC):
#     name: str
#     arguments: List[Argument]


# class Rule(BaseModel, ABC):
#     trigger: Condition
#     device: str
#     method: Method
#     release: Condition


class Datapoint(BaseModel):
    timestamp: datetime
    meas: Optional[Dict[str, Union[str, int, float]]] = None
    param: Optional[Dict[str, Union[str, int, float]]] = None

    @model_validator(mode="before")
    def check_meas_or_param(cls, values):
        meas, param = values.get("meas"), values.get("param")
        if meas is None and param is None:
            raise ValueError("Either meas or param must be provided")
        return values

    # use custom json encoder
    class Config:
        json_encoders = {datetime: convert_datetime}


# class AbstractMeasurement(BaseModel, ABC):
#     @field_validator("*", mode="before")
#     def check_fields(cls, v, field):
#         if isinstance(v, (int, float)):
#             # Check if there's any metadata other than 'ge' and 'le'
#             allowed_keys = {"ge", "le"}
#             extra_keys = set(field.field_info.extra.keys()) - allowed_keys
#             if extra_keys:
#                 raise ValueError(
#                     f"Field {field.name} has unsupported metadata: {extra_keys}"
#                 )
#         return v

#     def __init__(self, **data: Any):
#         # Dynamically create fields based on the subclass
#         fields = get_type_hints(self.__class__)
#         for name, type_ in fields.items():
#             self.__fields__[name] = type_
#         super().__init__(**data)


class AbstractMeasurement(BaseModel, ABC):
    @field_validator("*", mode="before")
    def check_fields(cls, value, field):
        if isinstance(value, (int, float)):
            pass
            # # Check if there's any metadata other than 'ge' and 'le'
            # allowed_keys = {"ge", "le"}
            # field_info = cls.model_fields[field.field_name].metadata
            # extra_keys = set(field_info.extra.keys()) - allowed_keys
            # if extra_keys:
            #     raise ValueError(
            #         f"Field {field} has unsupported metadata: {extra_keys}"
            #     )
        return value

    def __init__(self, **data: Any):
        # Dynamically create fields based on the subclass
        fields = get_type_hints(self.__class__)
        for name, type_ in fields.items():
            # Ensure fields are not overwritten if they already exist
            if name not in self.model_fields:
                self.model_fields[name] = type_
        super().__init__(**data)
