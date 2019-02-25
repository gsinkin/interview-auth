from flask import Flask, request, jsonify, g

from errors import BaseAPIError
from accounts import verify_account, create_account, login_required, logout_account
from database import init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/interview-auth.db"
init_db(app)


@app.route("/v3/accounts/login", methods=["POST"])
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


@app.route("/v3/accounts/logout", methods=["GET"])
@login_required
def logout():
    logout_account(g.account)
    return ("", 204)


@app.route("/v3/accounts", methods=["POST"])
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


@app.errorhandler(BaseAPIError)
def handle_base_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
