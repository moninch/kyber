from datetime import datetime, timezone

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (
    TokenAbsent, TokenExpired, UserNotFound
)
from app.users.dao import UsersDAO
from app.users.models import Users


def get_token(request: Request) -> str:
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsent

    return token


async def get_current_user(token: str = Depends(get_token)) -> Users:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )

    except JWTError:
        raise TokenAbsent

    expire: str = payload.get("exp")
    if not expire or int(expire) < datetime.now(timezone.utc).timestamp():
        raise TokenExpired

    user_id: str = payload.get("sub")
    if not user_id:
        raise UserNotFound

    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserNotFound

    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)) -> list[Users]:
    return await UsersDAO.find_all()
