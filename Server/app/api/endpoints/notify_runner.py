from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import create_notify_runner, read_user_notify_runner
from app.db import get_db
from app.schemas import NotifyRunner, NotifyRunnerCreate

router = APIRouter()


@router.post("/", response_model=NotifyRunner)
async def create(*, db: Session = Depends(get_db), notify_runner: NotifyRunnerCreate):
    return create_notify_runner(db, notify_runner=notify_runner)


@router.get("/{username}", response_model=NotifyRunner)
async def read(*, db: Session = Depends(get_db), username: str):
    return read_user_notify_runner(db, username)
