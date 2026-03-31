from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    HOST: str
    PORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"