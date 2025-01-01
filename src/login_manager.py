from flask_login import LoginManager

from app import get_app

app = get_app()
lm = LoginManager(app)