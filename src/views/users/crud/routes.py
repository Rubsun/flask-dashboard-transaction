from flask import Blueprint, request, jsonify, render_template
from sqlalchemy.exc import IntegrityError

from src import db
from src.db.models.user import User

user_crud = Blueprint("user_crud", __name__, url_prefix="/user")


@user_crud.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        form = request.form
        try:
            username = form["username"]
            password = form["password"]
            balance = form.get("balance", 0)
            commission_rate = form.get("commission_rate", 0)
            webhook_url = form.get("webhook_url", "")
            role = form.get("role", "user")

            new_user = User()
            new_user.username = username
            new_user.balance = balance
            new_user.commission_rate = commission_rate
            new_user.webhook_url = webhook_url
            new_user.role = role
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "User created successfully"}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": "Username already exists"}), 400
        except KeyError as e:
            return jsonify({"error": f"Missing field: {str(e)}"}), 400
    return render_template("user_create.html")


@user_crud.route("/update/<uuid:user_id>", methods=["GET", "POST"])
def update_user(user_id):
    if request.method == "GET":
        return render_template("update_user.html")
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    username = request.form.get("username")
    password = request.form.get("password")
    balance = request.form.get("balance")
    commission_rate = request.form.get("commission_rate")
    webhook_url = request.form.get("webhook_url")
    role = request.form.get("role")

    user.username = username
    user.set_password(password)
    user.balance = float(balance)
    user.commission_rate = float(commission_rate)
    user.webhook_url = webhook_url
    user.role = role
    db.session.commit()

    return jsonify({"message": "User updated successfully"})


@user_crud.route("/delete/<string:user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})
