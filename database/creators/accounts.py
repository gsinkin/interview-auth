from uuid import uuid4

import bcrypt
from sqlalchemy.exc import IntegrityError

from errors import BaseAPIError


def create_account(email, password):
    from database.models.accounts import db, Accounts
    lower_email = email.lower()
    api_key = str(uuid4())
    account = Accounts(
        email=lower_email,
        password_hash=bcrypt.hashpw(
            password.encode(), salt=bcrypt.gensalt(10)
        ),
        api_key=api_key,
    )

    try:
        db.session.add(account)
        db.session.commit()
    except IntegrityError:
        raise BaseAPIError("Account exists")
    return account
