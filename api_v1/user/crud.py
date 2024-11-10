from typing import Optional

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User


async def get_users(session: AsyncSession) -> list[User]:
    state = select(User).order_by(User.id)
    result: Result = await session.execute(state)
    users = result.scalars().all()
    return list(users)


async def get_item_users(session: AsyncSession, user_id: int) -> Optional[User]:
    return await session.get(User, user_id)


async def create_user(username: str, session: AsyncSession) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    return user