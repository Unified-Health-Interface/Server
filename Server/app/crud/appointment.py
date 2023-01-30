from sqlalchemy.orm import Session

from app import models, schemas


def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(username=appointment.username, doctor=appointment.doctor,
                                        hospital=appointment.hospital, date_time=appointment.date_time)
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def read_user_appointments(db: Session, username: str):
    return db.query(models.Appointment).filter(models.Appointment.username == username).all()
