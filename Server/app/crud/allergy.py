from app import models, schemas
from sqlalchemy.orm import Session


def create_allergy(db: Session, allergy: schemas.AllergyCreate):
    db_allergy = models.Allergy(username=allergy.username, allergy=allergy.allergy)
    db.add(db_allergy)
    db.commit()
    db.refresh(db_allergy)
    return db_allergy
