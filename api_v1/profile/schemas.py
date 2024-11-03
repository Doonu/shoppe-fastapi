from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class Profile(ProfileBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
