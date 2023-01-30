import datetime

from sqlalchemy import ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Bills(Base):
    __tablename__ = "bills"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    service: Mapped[str] = mapped_column(String)
    amount: Mapped[int] = mapped_column(Integer)
    due_date: Mapped[datetime.date] = mapped_column(Date)
    paid: Mapped[bool] = mapped_column(Boolean)

    username: Mapped[str] = mapped_column(ForeignKey("users.username"), unique=True)
