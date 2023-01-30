import datetime

from sqlalchemy import ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Prescription(Base):
    __tablename__ = "prescriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    doctor: Mapped[str] = mapped_column(String)
    date: Mapped[datetime.date] = mapped_column(Date)
    medicines: Mapped[str] = mapped_column(String)
    done: Mapped[bool] = mapped_column(Boolean)
    username: Mapped[str] = mapped_column(ForeignKey("users.username"))
