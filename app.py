from flask import Flask

from database import init_db


def create_app(db_uri):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    init_db(app)
    return app
