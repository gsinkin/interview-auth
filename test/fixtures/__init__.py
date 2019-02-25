import bcrypt


class BaseFixtures(object):

    model_class = None
    models = []


class AccountFixtures(BaseFixtures):

    from database.models.accounts import Accounts
    model_class = Accounts
    models = [
        dict(
            email="gabriel.sinkin@gmail.com",
            password_hash=bcrypt.hashpw(
                "Password1!".encode(), salt=bcrypt.gensalt(6)
            ),
            api_key="123-456-7890",
        ),
    ]
