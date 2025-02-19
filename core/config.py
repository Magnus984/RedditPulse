from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "RedditPulse"
    PROJECT_VERSION: str = "0.0.1"
    CLIENT_ID: str
    CLIENT_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()