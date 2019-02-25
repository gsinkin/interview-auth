from sqlalchemy.sql import func
from database import db


class Accounts(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    api_key = db.Column(db.String(60), nullable=False, unique=True)

    def __repr__(self):
        return '<Account %r>' % (
            self.email,
        )
