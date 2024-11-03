from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud

from .schemas import User

router = APIRouter(tags=["User"])


@router.get("/", response_model=List[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_users(session)


@router.post("/", response_model=User)
async def create_user(
    username: str,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(username=username, session=session)
