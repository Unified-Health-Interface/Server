from sqlalchemy.orm import Session

from app import models, schemas


def create_vaccination(db: Session, vaccination: schemas.VaccinationCreate):
    db_vaccination = models.Vaccination(username=vaccination.username, vaccine=vaccination.vaccine,
                                        date_time=vaccination.date_time, done=vaccination.done)
    db.add(db_vaccination)
    db.commit()
    db.refresh(db_vaccination)
    return db_vaccination


def read_user_vaccinations(db: Session, username: str, only_pending: bool):
    if only_pending:
        return db.query(models.Vaccination).filter(models.Vaccination.username == username).filter(
            models.Vaccination.done == False).all()

    return db.query(models.Vaccination).filter(models.Vaccination.username == username).all()
