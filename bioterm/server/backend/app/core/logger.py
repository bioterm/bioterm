import json
from contextlib import contextmanager
from functools import wraps

from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .....common.models.logs.database_models import LogEntry
from ...core.config import SQLALCHEMY_DATABASE_URI
from ..api.utils.security import User

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Assuming you have a function to get a database session
def get_db_session():
    return SessionLocal()


@contextmanager
def log_request(db_session, user_identifier, endpoint, parameters):
    log_entry = LogEntry(
        access_identifier=user_identifier, endpoint=endpoint, parameters=parameters
    )
    db_session.add(log_entry)
    db_session.commit()
    yield


def log_endpoint(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request", None)
        user: User = kwargs.get("current_user", None)

        user_identifier = user.email if user else "Unknown"
        endpoint_path = request.url.path if request else "Unknown"

        # Extract request method and parameters
        request_method = request.method if request else "Unknown"
        request_params = {}
        if request_method in ["GET", "DELETE"]:
            request_params = dict(request.query_params)
        elif request_method in ["POST", "PUT"]:
            # Reading the request body directly
            body = await request.body()
            try:
                request_params = json.loads(body)
            except json.JSONDecodeError:
                request_params = {"raw_body": body.decode()}

        with get_db_session() as session:
            with log_request(
                session,
                user_identifier,
                f"{request_method}: {endpoint_path}",
                request_params,
            ):
                return await func(*args, **kwargs)

    return wrapper
