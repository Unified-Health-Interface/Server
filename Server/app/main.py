from fastapi import FastAPI

from app.api import api_router
from app.core import settings
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)
