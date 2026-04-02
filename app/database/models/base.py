from uuid import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column

from uuid import uuid4


class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4()
    )