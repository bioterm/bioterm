import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String

from ..base import Base


class LogEntry(Base):
    __tablename__ = "log_entries"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    access_identifier = Column(String)
    endpoint = Column(String)
    parameters = Column(JSON)

    def __repr__(self):
        return (
            f"<LogEntry(timestamp={self.timestamp}, "
            f"user_identifier={self.user_identifier}, "
            f"parameters={self.parameters}, "
            f"endpoint={self.endpoint})>"
        )
