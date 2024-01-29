from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from ..base import Base


class DashboardModel(Base):
    __tablename__ = "dashboards"
    id = Column(Integer, primary_key=True, index=True)
    controller_id = Column(
        Integer, ForeignKey("controllers.id"), unique=True, index=True
    )
    uid = Column(String, unique=True)
    link = Column(String)

    controller = relationship(
        "ControllerModel", order_by="ControllerModel.id", back_populates="dashboards"
    )


class PanelModel(Base):
    __tablename__ = "panels"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), index=True)
    link = Column(String)
    hidden = Column(Boolean)

    devices = relationship(
        "DeviceModel", order_by="DeviceModel.id", back_populates="panels"
    )
