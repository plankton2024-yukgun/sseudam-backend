import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    # UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "images/")
    S3_BUCKET: str = os.getenv("S3_BUCKET")
    S3_REGION: str = os.getenv("S3_REGION")

    class Config:
        env_file = ".env"


settings = Settings()
