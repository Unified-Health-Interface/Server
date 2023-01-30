from sqlalchemy.orm import Session

from app import models, schemas


def create_bill(db: Session, bill: schemas.BillCreate):
    db_bill = models.Bill(username=bill.username, hospital=bill.hospital,
                          service=bill.service, amount=bill.amount,
                          due_date=bill.due_date, paid=bill.paid)
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill


def read_user_bill(db: Session, username: str, only_pending: bool):
    if only_pending:
        return db.query(models.Bill).filter(models.Bill.username == username).filter(
            models.Bill.paid == False).all()

    return db.query(models.Bill).filter(models.Bill.username == username).all()
