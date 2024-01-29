from typing import Dict
from typing import List
from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import Field

from ..rules.base_models import RulesDTO


class BaseMessage(BaseModel):
    controller: str


class RPCPayload(BaseModel):
    key: str
    params: Dict[str, Union[str, int, float]]


class RPCMessage(BaseMessage):
    type: Literal["rpc"]
    device: str
    rpc: RPCPayload


class RulesMessage(BaseMessage):
    type: Literal["rules"]
    rules: List[RulesDTO]


class MessageFromServer(BaseModel):
    message: Union[RPCMessage, RulesMessage] = Field(..., discriminator="type")


# # Union of different message types
# MessageFromServer: Union[RPCMessage, RulesMessage] = Field(..., discriminator="type")


# class MessageFromServer(BaseModel):
#     device: str
#     rpc: RPCPayload
