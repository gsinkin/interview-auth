import bcrypt
from flask import request, g

from errors import BaseAPIError
from database.updaters.accounts import invalidate_api_key
from database.loaders.accounts import get_account, get_by_api_key
from database.creators.accounts import create_account as db_create_account


def login_required(func, *args, **kwargs):
    def authenticate_request():
        api_key = request.headers.get('x-api-key')
        if not api_key:
            raise BaseAPIError("X-API-Key required")
        g.account = get_by_api_key(api_key)
        return func(*args, **kwargs)
    return authenticate_request


def verify_account(email, password):
    account = get_account(email)
    hashed = account.password_hash
    if bcrypt.hashpw(password.encode(), hashed) == hashed:
        return account
    raise BaseAPIError(
        "Invalid email or password",
        status_code=401,
    )


def create_account(email, password):
    return db_create_account(email, password)


def logout_account(account):
    invalidate_api_key(account)
