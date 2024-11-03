from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from typing import Optional

from .mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    _user_back_populates = "profile"
    _user_id_unique = True

    first_name: Mapped[Optional[str]] = mapped_column(String(40), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(40), nullable=True)
