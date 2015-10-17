from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    migrate = Migrate(app, db)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/')

    return app
