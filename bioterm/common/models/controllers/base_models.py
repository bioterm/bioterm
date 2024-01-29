from typing import Optional

from pydantic import BaseModel


class ControllerRegistration(BaseModel):
    uuid: str
    display_name: Optional[str] = None


class ControllerCreate(BaseModel):
    display_name: str
    description: Optional[str] = None


class ControllerUpdate(BaseModel):
    display_name: str
    description: Optional[str] = None
