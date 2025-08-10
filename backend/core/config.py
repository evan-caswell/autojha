from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    GEOCODE_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


# Cache function as env settings will not change
@lru_cache
def get_settings():
    return Settings()  # type: ignore
