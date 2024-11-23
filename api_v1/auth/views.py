from fastapi import APIRouter, Depends

from .dependencies import validate_auth_user
from .schemas import AuthBase
from .utils import encode_jwt
from ..user.schemas import User

router = APIRouter(tags=["Auth"])


@router.post("/login")
async def auth_login(user: User = Depends(validate_auth_user)):
    jwt_payload = {"username": user.username, "sub": user.id}
    access_token = encode_jwt(payload=jwt_payload)

    return AuthBase(access_token=access_token, token_type="Bearer")
