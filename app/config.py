from typing import Literal

from pydantic import Field, ValidationError, model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str = None

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY : str
    ALGORITHM : str

    @model_validator(mode='before')
    @classmethod
    def get_database_url(cls, values):
        values["DATABASE_URL"] = f"postgresql+asyncpg://{values['DB_USER']}:{values['DB_PASS']}@{values['DB_HOST']}:{values['DB_PORT']}/{values['DB_NAME']}"
        return values

    class Config:
        env_file = ".env"



settings = Settings()


