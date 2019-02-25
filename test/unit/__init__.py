from flask_testing import TestCase

from server import create_app, apply_routes


class BaseTestCase(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/interview-auth-tests.db"
    TESTING = True

    def create_app(self):
        app = create_app(self.SQLALCHEMY_DATABASE_URI)
        apply_routes(app)
        return app

    def setUp(self):
        from database.models.accounts import db
        db.create_all()

    def tearDown(self):
        from database.models.accounts import db
        db.session.remove()
        db.drop_all()
