from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Profile


async def get_profile(session: AsyncSession, user_id: int):
    result = await session.execute(select(Profile).filter(Profile.user_id == user_id))
    return result.scalars().first()


async def create_profile(
    session: AsyncSession,
    user_id: int,
    email: EmailStr,
    username: str,
    identity: int,
):
    profile = Profile(user_id=user_id, id=identity, email=email, username=username)
    session.add(profile)
    await session.commit()
    return profile
