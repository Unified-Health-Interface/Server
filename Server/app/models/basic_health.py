import datetime

from sqlalchemy import ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class BasicHealth(Base):
    __tablename__ = "vaccination"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer)
    dob: Mapped[datetime.date] = mapped_column(Date)
    sex: Mapped[str] = mapped_column(String)
    blood_group: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(ForeignKey("users.username"))
