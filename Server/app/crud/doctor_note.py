from sqlalchemy.orm import Session

from app import models, schemas


def create_doctor_note(db: Session, doctor_note: schemas.DoctorNoteCreate):
    db_doctor_note = models.DoctorNote(username=doctor_note.username, doctor=doctor_note.doctor,
                                       note=doctor_note.note)
    db.add(db_doctor_note)
    db.commit()
    db.refresh(db_doctor_note)
    return db_doctor_note


def read_user_doctor_note(db: Session, username: str):
    return db.query(models.DoctorNote).filter(models.DoctorNote.username == username).all()
