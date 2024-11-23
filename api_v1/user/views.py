from typing import List

from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .dependencies import user_by_id

from .schemas import User

router = APIRouter(tags=["User"])


@router.get("/", response_model=List[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_users(session)


@router.get("/{user_id}", response_model=User)
async def get_item_users(user: User = Depends(user_by_id)):
    return user


@router.post("/", response_model=User)
async def create_user(
    email: EmailStr,
    password: str,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(email=email, password=password, session=session)
