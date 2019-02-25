from flask_testing import TestCase

from server import create_app, apply_routes


class BaseTestCase(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/interview-auth-tests.db"
    TESTING = True
    FIXTURES = []

    def create_app(self):
        app = create_app(self.SQLALCHEMY_DATABASE_URI)
        apply_routes(app)
        return app

    def setUp(self):
        from database.models.accounts import db
        db.create_all()
        for fixture_class in self.FIXTURES:
            model_class = fixture_class.model_class
            for model in fixture_class.models:
                db.session.add(fixture_class.model_class(**model))
            db.session.commit()

    def tearDown(self):
        from database.models.accounts import db
        db.session.remove()
        db.drop_all()
