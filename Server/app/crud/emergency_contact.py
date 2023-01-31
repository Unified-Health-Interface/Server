from sqlalchemy.orm import Session

from app import models, schemas


def create_emergency_contact(db: Session, emergency_contact: schemas.EmergencyContactCreate):
    db_emergency_contact = models.EmergencyContact(username=emergency_contact.username, name=emergency_contact.name,
                                                   email=emergency_contact.email,
                                                   phone=emergency_contact.phone)
    db.add(db_emergency_contact)
    db.commit()
    db.refresh(db_emergency_contact)
    return db_emergency_contact


def read_user_emergency_contact(db: Session, username: str):
    return db.query(models.EmergencyContact).filter(models.EmergencyContact.username == username).all()
