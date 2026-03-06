from functools import wraps
from flask import request, jsonify
import jwt

SECRET_KEY = "SECRET"


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"message": "Token missing"}), 401

        try:

            token = auth_header.split(" ")[1]

            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        except Exception:
            return jsonify({"message": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated