from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import db
from src.db.models.mixins import UUIDMixin, CreatedAtMixin


class Transaction(db.Model, UUIDMixin, CreatedAtMixin):
    amount: Mapped[float] = mapped_column(nullable=False, default=0)
    commission: Mapped[float] = mapped_column(nullable=False, default=0)
    status: Mapped[str] = mapped_column(nullable=False, default="pending")
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="transactions")
