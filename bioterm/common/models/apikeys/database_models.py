from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from ..base import Base


class APIKeyModel(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)
    controller_id = Column(Integer, ForeignKey("controllers.id"), index=True)
    created = Column(DateTime(timezone=True))
    revoked = Column(Boolean)

    controller = relationship("ControllerModel", back_populates="api_keys")
