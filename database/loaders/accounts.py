from errors import BaseAPIError


def get_account(email):
    from database.models.accounts import db, Accounts
    lower_email = email.lower()
    account = db.session.query(Accounts).filter(
        Accounts.email == lower_email
    ).first()
    if not account:
        raise BaseAPIError(
            "Invalid email or password",
            status_code=401,
        )
    return account


def get_by_api_key(api_key):
    from database.models.accounts import db, Accounts
    account = db.session.query(Accounts).filter(
        Accounts.api_key == api_key
    ).first()
    if not account:
        raise BaseAPIError(
            "Invalid API Key"
        )
    return account
