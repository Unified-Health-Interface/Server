from sqlalchemy.orm import Session

from app import models, schemas


def create_vaccination(db: Session, vaccination: schemas.VaccinationCreate):
    db_vaccination = models.Vaccination(username=vaccination.username, vaccine=vaccination.vaccine,
                                        date=vaccination.date)
    db.add(db_vaccination)
    db.commit()
    db.refresh(db_vaccination)
    return db_vaccination


def read_user_vaccinations(db: Session, username: str):
    return db.query(models.Vaccination).filter(models.Vaccination.username == username).all()
