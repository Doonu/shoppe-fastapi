from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = "postgresql+asyncpg://postgres:qwerty@localhost:5436/"
    echo: bool = True


settings = Settings()
