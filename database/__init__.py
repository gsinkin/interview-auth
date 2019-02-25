from flask_sqlalchemy import SQLAlchemy

db = None


def init_db(app):
    global db
    db = SQLAlchemy(app)
    db.create_all()
    with app.app_context():
        with app.open_resource('schema.sql', mode='r') as f:
            db.engine.execute(f.read())
