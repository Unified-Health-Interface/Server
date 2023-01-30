import datetime

from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    doctor: Mapped[str] = mapped_column(String)
    hospital: Mapped[str] = mapped_column(String)
    date_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    username: Mapped[str] = mapped_column(ForeignKey("users.username"))
