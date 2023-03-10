from sqlalchemy.orm import Session

from app import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
