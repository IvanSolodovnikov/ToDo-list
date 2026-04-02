from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, String


from .base import Base

class TaskORM(Base):
    __tablename__ = "tasks"

    text: Mapped[str] = mapped_column(String(255), nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)