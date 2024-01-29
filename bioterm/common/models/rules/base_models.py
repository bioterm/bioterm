# from abc import ABC
from datetime import datetime
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated

# from typing import Dict


class BaseCondition(BaseModel):
    dwell: Optional[float] = None


class LogicCondition(BaseCondition):
    operator: Literal["AND", "OR"]
    conditions: List["Condition"]  # union defined below


class ValueCondition(BaseCondition):
    device: str
    meas: str
    value: Union[str, int, float]
    operator: Literal["eq", "le", "leq", "ge", "geq", "neq"]


class TimeCondition(BaseCondition):
    value: float
    operator: Literal["time"] = "time"


Condition = Annotated[
    Union[LogicCondition, ValueCondition, TimeCondition],
    Field(discriminator="operator"),
]


class Argument(BaseModel):
    name: str
    value: Union[str, int, float]


class Method(BaseModel):
    name: str
    arguments: List[Argument]


class Rule(BaseModel):
    device: str
    trigger_condition: Condition
    trigger_method: Method
    release_condition: Condition
    release_method: Method


class RuleCreate(BaseModel):
    sync: bool
    display_name: str
    description: str
    rule: Rule


class RuleUpdate(BaseModel):
    sync: bool
    display_name: str
    description: str
    rule: Rule


class RuleState(BaseModel):
    # uuid: str
    active: bool = False
    triggering: bool = False
    triggered_since: Optional[datetime] = None
    releasing: bool = False
    released_since: Optional[datetime] = None


class RulesDTO(Rule):
    uuid: str
