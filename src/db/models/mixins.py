from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src import db


class UUIDMixin(db.Model):
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, nullable=False)


class CreatedAtMixin(db.Model):
    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
