from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from ..base import Base


class ControllerModel(Base):
    __tablename__ = "controllers"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, index=True)
    display_name = Column(String, index=True)
    registration_date = Column(DateTime(timezone=True))
    description = Column(String)

    api_keys = relationship(
        "APIKeyModel", order_by="APIKeyModel.id", back_populates="controller"
    )
    devices = relationship(
        "DeviceModel", order_by="DeviceModel.id", back_populates="controller"
    )
    dashboards = relationship(
        "DashboardModel", order_by="DashboardModel.id", back_populates="controller"
    )

    rules = relationship(
        "RuleModel", order_by="RuleModel.id", back_populates="controller"
    )
