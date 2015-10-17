from flask import jsonify, current_app
from flask.ext.sqlalchemy import get_debug_queries

from . import app, db
from .models import User, Item, Order, ItemTag, OrderTag


@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= current_app.config['SLOW_DB_QUERY_TIME']:
            current_app.logger.warning(
                'Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
                % (query.statement, query.parameters, query.duration,
                   query.context))
    return response


@app.route('/getOrder')
def get_order():
    return jsonify(Users=['wei', 'hai', 'dkjfk'])


@app.route('/')
def users():
    users = User.query.all()
    return jsonify(Users=[u.serialize for u in users])

