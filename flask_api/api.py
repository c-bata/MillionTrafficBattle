from flask import jsonify, current_app
from flask.ext.sqlalchemy import get_debug_queries

from . import app, db
from .models import User, Item, Order, Tag


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


@app.route('/initialize')
def initialize():
    import csv

    db.drop_all()
    db.create_all()

    # user.tsv
    f = open(current_app.config['DATA_DIR'] + 'user.tsv')
    tsv = csv.reader(f, delimiter='\t')

    for i, row in enumerate(tsv):
        if i == 0:
            continue
        user = User(row[0], row[1], row[2])
        db.session.add(user)
    db.session.commit()

    # item.tsv
    f = open(current_app.config['DATA_DIR'] + 'item.tsv')
    tsv = csv.reader(f, delimiter='\t')

    for i, row in enumerate(tsv):
        if i == 0:
            continue
        item = Item(row[0], row[1], row[2], row[3])
        db.session.add(item)
    db.session.commit()

    # order.tsv
    f = open(current_app.config['DATA_DIR'] + 'order.tsv')
    tsv = csv.reader(f, delimiter='\t')

    for i, row in enumerate(tsv):
        if i == 0:
            continue
        order = Order(row[0], row[1], row[2], row[3], row[4], row[5])
        db.session.add(order)
    db.session.commit()

    return 'Success'


@app.route('/')
def users():
    users = User.query.all()
    return jsonify(Users=[u.serialize for u in users])
