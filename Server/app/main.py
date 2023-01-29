from app.api import api_router
from app.core import settings
from fastapi import FastAPI

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)
