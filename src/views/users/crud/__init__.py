from flask import Blueprint

from . import routes

user_crud = Blueprint("user", __name__)
