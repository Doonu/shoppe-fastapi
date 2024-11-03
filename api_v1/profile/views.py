from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status

from core.models import db_helper

from . import crud
from .schemas import Profile

router = APIRouter(tags=["Profile"])


@router.get("/{user_id}", response_model=Profile)
async def get_profile(
    user_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_profile(session=session, user_id=user_id)
