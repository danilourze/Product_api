from flask import Blueprint, request, jsonify
import jwt
import datetime

auth_bp = Blueprint("auth", __name__)

SECRET_KEY = "super_secret_key"


@auth_bp.route("/auth/login", methods=["POST"])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    # login mockado (para teste técnico)
    if username == "admin" and password == "123":

        token = jwt.encode(
            {
                "user": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            },
            SECRET_KEY,
            algorithm="HS256"
        )

        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401