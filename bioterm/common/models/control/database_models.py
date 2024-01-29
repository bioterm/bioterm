# from sqlalchemy import Column
# from sqlalchemy import ForeignKey
# from sqlalchemy import Integer
# from sqlalchemy import String
# from sqlalchemy import Boolean
# from sqlalchemy.dialects.postgresql import JSONB
# from sqlalchemy.orm import relationship
# from ..base import Base
# class RuleModel(Base):
#     __tablename__ = "rules"
#     id = Column(Integer, primary_key=True, index=True)
#     uuid = Column(String, unique=True, index=True)
#     active = Column(Boolean)
#     controller_id = Column(Integer, ForeignKey("controllers.id"), index=True)
#     display_name = Column(String, index=True)
#     description = Column(String)
#     rule = Column(JSONB)
#     controller = relationship(
#         "ControllerModel", order_by="ControllerModel.id", back_populates="rules"
#     )
