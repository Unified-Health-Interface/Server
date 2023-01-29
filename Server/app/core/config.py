import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "UHI"
    SQLALCHEMY_DATABASE_URL = "sqlite:///./UHI.db"


settings = Settings()
