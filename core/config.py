import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings
from pydantic import BaseModel

env_file = ".env.dev" if os.getenv("ENV") == "dev" else ".env.prod"
load_dotenv(env_file)


class DbSetting(BaseModel):
    print(os.getenv("DATABASE_URL"))
    url: str = os.getenv("DATABASE_URL")
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DbSetting = DbSetting()


settings = Settings()
