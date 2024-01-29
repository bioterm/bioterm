from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from ..base import Base


class LegalContent(Base):
    __tablename__ = "legal_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    legal = Column(Text, nullable=False)
