from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import get_base_profile
from .schemas import Profile

http_bearer = HTTPBearer()
router = APIRouter(tags=["Profile"], dependencies=[Depends(http_bearer)])


@router.get("/{user_id}", response_model=Profile)
async def get_profile(
    profile: AsyncSession = Depends(get_base_profile),
):
    return profile


@router.get("/", response_model=List[Profile])
async def get_profile_list(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_profile_list(session=session)
