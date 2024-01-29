from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from ..base import Base


class DeviceModel(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, index=True)
    controller_id = Column(Integer, ForeignKey("controllers.id"), index=True)
    display_name = Column(String, index=True)
    registration_date = Column(DateTime(timezone=True))
    description = Column(String)
    parameters = Column(JSONB)
    measurement_model = Column(JSONB)
    parameter_model = Column(JSONB)
    rpc = Column(JSONB)

    controller = relationship(
        "ControllerModel", order_by="ControllerModel.id", back_populates="devices"
    )
    panels = relationship(
        "PanelModel", order_by="PanelModel.id", back_populates="devices"
    )
