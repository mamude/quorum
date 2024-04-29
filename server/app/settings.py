from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_TITLE: str
    VERSION: str

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
