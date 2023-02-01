from sqlalchemy.orm import Session

from app import models, schemas


def create_notify_runner(db: Session, notify_runner: schemas.NotifyRunnerCreate):
    db_notify_runner = models.NotifyRunner(username=notify_runner.username, endpoint=notify_runner.endpoint)
    db.add(db_notify_runner)
    db.commit()
    db.refresh(db_notify_runner)
    return db_notify_runner


def read_user_notify_runner(db: Session, username: str):
    return db.query(models.NotifyRunner).filter(models.NotifyRunner.username == username).first()
