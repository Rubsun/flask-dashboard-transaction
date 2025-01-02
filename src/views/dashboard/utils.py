from datetime import datetime, date

from sqlalchemy import func

from src import db
from src.db.models.transaction import Transaction


def amount_transaction_on_day(date: date) -> float:
    start_of_day = datetime.combine(date, datetime.min.time())
    end_of_day = datetime.combine(date, datetime.max.time())

    amount = (
        db.session.query(func.sum(Transaction.amount))
        .filter(
            Transaction.created_at >= start_of_day, Transaction.created_at <= end_of_day
        )
        .scalar()
    )

    return amount or 0
