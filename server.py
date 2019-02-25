from flask import Flask, request, jsonify, g

from app import create_app
from errors import BaseAPIError
from accounts import verify_account, create_account, login_required, \
    logout_account


def login():
    request_data = request.json
    email = request_data.get("email")
    password = request_data.get("password")
    if not email or not password:
        raise BaseAPIError(
            "email and password required",
            status_code=401,
        )
    account = verify_account(email, password)
    return jsonify({"api_key": account.api_key})


@login_required
def logout():
    logout_account(g.account)
    return ("", 204)


def new_account():
    request_data = request.json
    email = request_data.get("email")
    password = request_data.get("password")
    if not email or not password:
        raise BaseAPIError(
            "email and password required",
            status_code=400,
        )
    account = create_account(email, password)
    return jsonify({"api_key": account.api_key})


def handle_base_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def apply_routes(app):
    app.add_url_rule("/v3/accounts/login", "login", login, methods=["POST"])
    app.add_url_rule("/v3/accounts/logout", "logout", logout, methods=["GET"])
    app.add_url_rule(
        "/v3/accounts", "new_account", new_account,
        methods=["POST"]
    )
    app.register_error_handler(BaseAPIError, handle_base_error)


if __name__ == "server":
    app = create_app("sqlite:////tmp/interview-auth.db")
    apply_routes(app)
