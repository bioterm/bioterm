from pydantic import BaseModel


class LegalContentSchema(BaseModel):
    legal: str
