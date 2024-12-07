from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import get_base_profile
from .schemas import Profile

http_bearer = HTTPBearer()
router = APIRouter(tags=["Profile"], dependencies=[Depends(http_bearer)])


@router.get("/{user_id}", response_model=Profile)
async def get_profile(
    profile: AsyncSession = Depends(get_base_profile),
):
    return profile
