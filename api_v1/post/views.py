from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import PostsGet, PostCreate

router = APIRouter(tags=["Post"])


@router.get("/", response_model=list[PostsGet])
async def get_post(
    user_id: Optional[int] = None,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_all_posts(session=session, user_id=user_id)


@router.post("/")
async def create_post(
    post_in: PostCreate,
    user_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_post(session=session, post_in=post_in, user_id=user_id)
