from typing import Any
from flask import jsonify, request, Blueprint

import json

user_blueprint = Blueprint("user_api", __name__)



with open("users.json") as file:
    data = json.load(file)


@user_blueprint.route("/api/user")
def get_all_users():
    return jsonify(list[data])


@user_blueprint.route("/api/user", methods=["POST"])
def create_new_user():
    """Register a new user."""

    new_user: dict[str, Any] = request.json

    try:
        assert isinstance(create_new_user, dict), "Invalid type"
        assert "login" in create_new_user
        assert "password" in create_new_user
        assert len(create_new_user["password"]) > 0
    except AssertionError:
        return jsonify({"info": "Invalid data format"}), 422

    with open("users.json") as file:
        data = json.load(file)

    data[create_new_user["login"]] = {"password": create_new_user["password"]}
    with open("users.json", "w") as file:
        json.dump(data, file)

    return jsonify({"info": "Success"})