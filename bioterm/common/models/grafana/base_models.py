from typing import Optional

from pydantic import BaseModel


class DashboardCreate(BaseModel):
    controller_id: Optional[int] = None
    uid: Optional[str] = None
    link: str


class DashboardUpdate(BaseModel):
    controller_id: int
    link: str


class PanelCreate(BaseModel):
    device_id: int
    link: str
    hidden: bool


class PanelUpdate(BaseModel):
    device_id: int
    link: str
    hidden: bool
