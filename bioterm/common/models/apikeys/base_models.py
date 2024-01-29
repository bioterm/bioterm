from typing import Optional

from pydantic import BaseModel


class APIKeyCreate(BaseModel):
    controller_id: Optional[int] = None


class APIKeyUpdate(BaseModel):
    controller_id: Optional[int] = None
    revoked: bool
