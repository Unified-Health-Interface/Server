from sqlalchemy import ForeignKey, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class NotifyRunner(Base):
    __tablename__ = "notify_runner"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    endpoint: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(ForeignKey("users.username"), unique=True)
