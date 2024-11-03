from pydantic_settings import BaseSettings
from pydantic import BaseModel


class DbSetting(BaseModel):
    url: str = "postgresql+asyncpg://postgres:qwerty@localhost:5436/"
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DbSetting = DbSetting()


settings = Settings()
