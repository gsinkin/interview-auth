from uuid import uuid4


def invalidate_api_key(account):
    from database.models.accounts import db
    account.api_key = str(uuid4())
    db.session.commit()
