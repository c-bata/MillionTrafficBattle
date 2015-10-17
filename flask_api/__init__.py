from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from .models import db
    db.init_app(app)

    from .api import app as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/')

    return app
