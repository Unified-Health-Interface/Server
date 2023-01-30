from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "UHI"
    SQLALCHEMY_DATABASE_URL = "sqlite:///app/UHI.db"


settings = Settings()
