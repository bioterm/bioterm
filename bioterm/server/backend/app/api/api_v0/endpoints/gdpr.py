from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .......common.core.logger import get_module_logger
from .......common.models.gdpr.base_models import LegalContentSchema
from .......common.models.gdpr.database_models import LegalContent
from .....core.config import SQLALCHEMY_DATABASE_URI
from ...utils.security import credentials_noadmin_exception
from ...utils.security import User
from ...utils.security import validate

router = APIRouter()
logger = get_module_logger(__name__)

# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@router.get("/", tags=["gdpr"])
async def read_legal_content():
    db = SessionLocal()
    content = db.query(LegalContent).first()
    if content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return content


@router.put("/", tags=["gdpr"])
async def update_legal_content(
    content_data: LegalContentSchema, current_user: User = Depends(validate)
):
    if "authentik Admins" not in current_user.groups:
        raise credentials_noadmin_exception
    db = SessionLocal()
    content = db.query(LegalContent).first()
    if content is None:
        content = LegalContent()
        db.add(content)
    content.legal = content_data.legal
    db.commit()
    return content
