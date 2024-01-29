import json
from typing import List
from typing import Optional
from typing import Union

from fastapi import Depends
from fastapi import HTTPException
from fastapi import Security
from fastapi import status
from fastapi import WebSocket
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.security.api_key import APIKeyHeader
from jose import jwt
from jose import JWTError
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy import not_
from sqlalchemy.orm import sessionmaker
from starlette.status import HTTP_403_FORBIDDEN

from ......common.core.logger import get_module_logger
from ......common.models.apikeys.database_models import APIKeyModel
from ....core.config import AUTHENTIK_CLIENT_ID
from ....core.config import AUTHENTIK_PUBLIC_KEY
from ....core.config import AUTHENTIK_URL
from ....core.config import SQLALCHEMY_DATABASE_URI


logger = get_module_logger(__name__)

# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

api_key_header = APIKeyHeader(name="access-token", auto_error=False)
ALGORITHM = "RS256"

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{AUTHENTIK_URL}/application/o/authorize/",
    tokenUrl=f"{AUTHENTIK_URL}/application/o/token/",
    # scopes={"email", "openid", "profile"},
)


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    groups: Union[List[str], None] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


credentials_noadmin_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="You do not have administrator access",
    headers={"WWW-Authenticate": "Bearer"},
)

credentials_validation_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def validate(token: str = Depends(oauth2_scheme)):
    logger.debug(f"Received token: {token}")
    try:
        payload = jwt.decode(
            token,
            AUTHENTIK_PUBLIC_KEY,
            algorithms=[ALGORITHM],
            audience=AUTHENTIK_CLIENT_ID,
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_validation_exception
        # token_data = TokenData(username=username)
    except JWTError:
        raise credentials_validation_exception
    return User(
        email=payload.get("email"),
        username=payload.get("preferred_username"),
        groups=payload.get("groups"),
    )


async def get_api_key(api_key_header: str = Security(api_key_header)):
    db = SessionLocal()
    api_keys = (
        db.query(APIKeyModel.key)
        .filter(not_(APIKeyModel.revoked))
        .filter(APIKeyModel.key == api_key_header)
        .first()
    )
    db.close()
    if api_keys:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )


async def extract_api_key(json_string: str) -> str:
    try:
        data = json.loads(json_string)
        return data.get("api_key", None)
    except json.JSONDecodeError:
        return None


async def get_api_key_ws(websocket: WebSocket) -> Optional[str]:
    # Extract headers directly from WebSocket's scope
    headers = dict(websocket.scope.get("headers", []))

    # Convert headers from byte to string
    auth_header = headers.get(b"authorization", b"").decode("utf-8")

    # Expect the header to be in the format "Bearer {API_KEY}"
    if not auth_header.startswith("Bearer "):
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return None

    apikey = auth_header.split(" ", 1)[1]
    if not apikey:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return None

    return apikey
