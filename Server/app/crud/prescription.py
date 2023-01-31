from sqlalchemy.orm import Session

from app import models, schemas


def create_prescription(db: Session, prescription: schemas.PrescriptionCreate):
    db_prescription = models.Prescription(username=prescription.username, doctor=prescription.doctor,
                                          medicines=prescription.medicines,
                                          date_time=prescription.date_time, done=prescription.done)
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription


def read_user_prescription(db: Session, username: str, only_pending: bool):
    if only_pending:
        return db.query(models.Prescription).filter(models.Prescription.username == username).filter(
            models.Prescription.done == False).all()

    return db.query(models.Prescription).filter(models.Prescription.username == username).all()
