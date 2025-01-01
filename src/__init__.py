from celery import Celery
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import setup_app
from config.settings import settings
from src.db.models.meta import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
celery = Celery(__name__, broker=settings.redis_url)


def create_app():
    app = Flask(__name__)
    setup_app(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = settings.DB_PASSWORD

    db.init_app(app)
    migrate.init_app(app, db)

    # with app.app_context():
    #     from .routes import dashboard, users, transactions
    #
    #     app.register_blueprint(dashboard.bp)
    #     app.register_blueprint(users.bp)
    #     app.register_blueprint(transactions.bp)

    return app


celery.conf.update({"result_backend": settings.redis_url})

