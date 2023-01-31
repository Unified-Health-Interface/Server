import datetime

from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Vaccination(Base):
    __tablename__ = "vaccination"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    vaccine: Mapped[str] = mapped_column(String)
    date_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    done: Mapped[bool] = mapped_column(Boolean)
    username: Mapped[str] = mapped_column(ForeignKey("users.username"))
