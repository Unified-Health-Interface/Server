import os

from dotenv import load_dotenv


class Settings:
    PROJECT_NAME = "UHI"
    DATABASE_USERNAME = os.environ.get("DATABASE_USER")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@localhost/UHI"
    )


settings = Settings()
