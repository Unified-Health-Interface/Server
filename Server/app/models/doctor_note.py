from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class DoctorNote(Base):
    __tablename__ = "doctor_notes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    doctor: Mapped[str] = mapped_column(String)
    note: Mapped[str] = mapped_column(String)

    username: Mapped[str] = mapped_column(ForeignKey("users.username"))
