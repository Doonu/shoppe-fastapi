from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Profile


async def get_profile(session: AsyncSession, user_id: int):
    result = await session.execute(select(Profile).filter(Profile.user_id == user_id))
    profile = result.scalars().first()

    if not profile:
        profile = Profile(user_id=user_id)
        session.add(profile)
        await session.commit()

    return profile
