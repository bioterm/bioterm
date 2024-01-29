import secrets
from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .......common.core.logger import get_module_logger
from .......common.models.apikeys.base_models import APIKeyCreate
from .......common.models.apikeys.base_models import APIKeyUpdate
from .......common.models.apikeys.database_models import APIKeyModel
from .....core.config import SQLALCHEMY_DATABASE_URI
from ....core.metadata import generate_metadata
from ...utils.security import credentials_noadmin_exception
from ...utils.security import User
from ...utils.security import validate

router = APIRouter()
logger = get_module_logger(__name__)

# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@router.post("/", tags=["apikeys"])
async def create_apikey(api_key: APIKeyCreate, current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    generated_key = secrets.token_urlsafe(20)
    new_key = APIKeyModel(
        key=generated_key, created=datetime.now(), revoked=False, **api_key.dict()
    )
    db.add(new_key)
    db.commit()
    db.refresh(new_key)
    db.close()
    return new_key


@router.get("/", tags=["apikeys"])
async def read_apikeys(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    api_keys = db.query(APIKeyModel).all()
    db.close()
    return api_keys


@router.put("/{api_key_id}", tags=["apikeys"])
async def update_apikey(
    api_key_id: int, api_key: APIKeyUpdate, current_user: User = Depends(validate)
):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_api_key = db.query(APIKeyModel).filter(APIKeyModel.id == api_key_id).first()
    if not db_api_key:
        db.close()
        raise HTTPException(status_code=404, detail="APIKey not found")
    for key, value in api_key.dict().items():
        setattr(db_api_key, key, value)
    db.commit()
    db.close()
    return db_api_key


@router.delete("/{api_key_id}", tags=["apikeys"])
async def delete_apikey(api_key_id: int, current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    db_api_key = db.query(APIKeyModel).filter(APIKeyModel.id == api_key_id).first()
    if not db_api_key:
        db.close()
        raise HTTPException(status_code=404, detail="APIKey not found")
    db.delete(db_api_key)
    db.commit()
    db.close()
    return {"status": "success"}


@router.get("/metadata", tags=["apikeys"])
async def get_metadata(current_user: User = Depends(validate)):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    form_elements_create = generate_metadata(APIKeyCreate)
    form_elements_update = generate_metadata(APIKeyUpdate)

    # Generate column info based on APIKey SQLAlchemy model's columns
    columns = [
        {
            "name": column.name,
            "label": column.name.upper(),
            "field": column.name,
            "align": "left",
            "sortable": True if column.primary_key else False,
        }
        for column in APIKeyModel.__table__.columns
    ]

    return {
        "formElementsUpdate": form_elements_update,
        "formElementsCreate": form_elements_create,
        "columns": columns,
    }
