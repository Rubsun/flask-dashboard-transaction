from typing import List, Optional

from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash

from db.models.transaction import Transaction
from src import db
from src.db.models.mixins import UUIDMixin


class User(db.Model, UUIDMixin, UserMixin):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    password_hash: Mapped[Optional[str]]

    balance: Mapped[float] = mapped_column(nullable=False, default=0)
    commission_rate: Mapped[float] = mapped_column(nullable=False, default=0)
    webhook_url: Mapped[str] = mapped_column(nullable=False, default="")
    role: Mapped[str] = mapped_column(nullable=False, default="user")
    transaction: Mapped[List[Transaction]] = relationship(back_populates="user")

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
