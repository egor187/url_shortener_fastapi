from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    SQL_ALCHEMY_URL: str = ...
    DEFAULT_REDIRECT_URL: str = 'https://www.google.com'
    DEFAULT_SHORT_CODE_LENGTH: int = 7

    class Config:
        env_file = '.env'


@lru_cache
def get_settings() -> Settings:
    return Settings()
