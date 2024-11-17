from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from api_v1.post.schemas import PostCreate
from core.models import Post


async def create_post(session: AsyncSession, post_in: PostCreate, user_id: int) -> Post:
    post = Post(**post_in.model_dump(), user_id=user_id)
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


async def get_all_posts(session: AsyncSession, user_id: Optional[int] = None):
    state = (
        select(Post)
        .options(joinedload(Post.user))
        .where(Post.user_id == user_id if user_id else True)
        .order_by(Post.id)
    )

    posts = await session.scalars(state)
    return list(posts)
