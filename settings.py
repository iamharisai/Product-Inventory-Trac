# settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "telusko"

    class Config:
        env_file = ".env"        # local .env file is optional but convenient
        env_file_encoding = "utf-8"

settings = Settings()