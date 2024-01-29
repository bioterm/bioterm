from typing import Dict
from typing import Optional

from pydantic import BaseModel


class DeviceRegistration(BaseModel):
    uuid: str
    display_name: Optional[str] = None
    description: Optional[str] = None
    parameters: Dict
    measurement_model: Dict
    parameter_model: Dict
    rpc: Dict

    class Config:
        arbitrary_types_allowed = True


class DeviceCreate(BaseModel):
    controller_id: int
    display_name: str
    description: Optional[str] = None


class DeviceUpdate(BaseModel):
    controller_id: int
    display_name: str
    description: Optional[str] = None
