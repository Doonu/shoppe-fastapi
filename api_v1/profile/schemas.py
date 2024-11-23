from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class ProfileBase(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr


class Profile(ProfileBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
