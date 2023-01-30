from sqlalchemy.orm import Session

from app import models, schemas


def create_basic_health(db: Session, basic_health: schemas.BasicHealthCreate):
    db_basic_health = models.BasicHealth(username=basic_health.username, age=basic_health.age,
                                         dob=basic_health.dob, sex=basic_health.sex,
                                         blood_group=basic_health.blood_group)
    db.add(db_basic_health)
    db.commit()
    db.refresh(db_basic_health)
    return db_basic_health


def read_user_basic_health(db: Session, username: str):
    return db.query(models.BasicHealth).filter(models.BasicHealth.username == username).first()
