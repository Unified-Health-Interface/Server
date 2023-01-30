from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Allergy(Base):
    __tablename__ = "allergy"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    allergy: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(ForeignKey("users.username"))
