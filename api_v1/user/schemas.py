from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: Optional[str]
    password: bytes
    email: EmailStr


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
