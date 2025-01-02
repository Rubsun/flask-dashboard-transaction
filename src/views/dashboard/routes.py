from datetime import datetime

from flask import render_template
from sqlalchemy import select

from db.models.transaction import Transaction
from db.models.user import User
from src import db
from views.dashboard import dashboard
from views.dashboard.utils import amount_transaction_on_day


@dashboard.route("/")
def dashboard() -> str:
    users_count = User.query.count()
    transactions_count = Transaction.query.count()
    transactions_amount = amount_transaction_on_day(datetime.now().date())
    transactions_limit = db.session.scalars(
        select(Transaction).order_by(Transaction.date).limit(10)
    )
    return render_template(
        "dashboard_main.html",
        users_count=users_count,
        transactions_count=transactions_count,
        transactions_amount=transactions_amount,
        transactions_limit=transactions_limit,
    )
