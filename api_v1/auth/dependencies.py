from fastapi import Form, HTTPException, status, Depends

from api_v1.auth.utils import validate_password
from api_v1.user.crud import get_item_users_by_email
from api_v1.user.schemas import User


async def validate_auth_user(
    user: User = Depends(get_item_users_by_email),
    password: str = Form(),
):
    authed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный логин или пароль"
    )

    if not user:
        raise authed_exc

    if not validate_password(password_user=password, hashed_password=user.password):
        raise authed_exc

    return user
