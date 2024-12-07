from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api_v1.user import crud
from core.models import Profile


async def get_profile(session: AsyncSession, user_id: int):
    result = await session.execute(select(Profile).filter(Profile.user_id == user_id))
    profile = result.scalars().first()

    if profile is not None:
        return profile

    user = await crud.get_item_users(session=session, user_id=user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    profile = Profile(
        user_id=user_id, id=user.id, email=user.email, username=user.username
    )
    session.add(profile)
    await session.commit()
    return profile
