from pydantic import BaseModel, ConfigDict


class AuthBase(BaseModel):
    access_token: str
    token_type: str
