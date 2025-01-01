from db.models.user import User
from login_manager import lm
from src import db


@lm.user_loader
def load_user(id: str) -> User:
    return db.session.get(User, id)
