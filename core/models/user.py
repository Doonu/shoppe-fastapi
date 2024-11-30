from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, LargeBinary
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .post import Post


class User(Base):
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String(32), nullable=True)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
