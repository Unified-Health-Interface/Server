from app import models, schemas

from sqlalchemy.orm import Session


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
