import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL

load_dotenv()


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

    def get_database_url(self):
        return URL.create(
            drivername=f"postgresql+asyncpg",
            host=self.POSTGRES_HOST,
            password=self.POSTGRES_PASSWORD,
            username=self.POSTGRES_USER,
            database=self.POSTGRES_USER,
            port=self.POSTGRES_PORT,
        ).render_as_string(hide_password=False)

    def get_api_key(self):
        return self.API_KEY
