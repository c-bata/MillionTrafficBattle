from flask import jsonify, current_app, request
from flask.ext.sqlalchemy import get_debug_queries

from . import app, db
from .models import User, Item, Order


@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= current_app.config['SLOW_DB_QUERY_TIME']:
            current_app.logger.warning(
                'Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
                % (query.statement, query.parameters, query.duration,
                   query.context))
    return response


@app.route('/searchOrder')
def get_order():
    findByOrderDateTimeGTE = request.args.get('findByOrderDateTimeGTE')
    findByOrderDateTimeLTE = request.args.get('findByOrderDateTimeLTE')
    findByOrderUserId = request.args.get('findByOrderUserId')
    findByOrderItemId = request.args.get('findByOrderItemId')
    findByOrderQuantityGTE = request.args.get('findByOrderQuantityGTE')
    findByOrderQuantityLTE = request.args.get('findByOrderQuantityLTE')
    findByOrderState = request.args.get('findByOrderState')
    findByOrderTagsIncludeAll = request.args.get('findByOrderTagsIncludeAll')
    findByOrderTagsIncludeAny = request.args.get('findByOrderTagsIncludeAny')

    order_query = Order.query
    if findByOrderDateTimeGTE:
        order_query = order_query.filter(Order.order_date_time >= int(findByOrderDateTimeGTE))

    if findByOrderDateTimeLTE:
        order_query = order_query.filter(Order.order_date_time <= int(findByOrderDateTimeGTE))

    if findByOrderUserId:
        order_query = order_query.filter(Order.order_user_id == findByOrderUserId)

    if findByOrderItemId:
        order_query = order_query.filter(Order.order_item_id == findByOrderItemId)

    if findByOrderQuantityGTE:
        order_query = order_query.filter(Order.order_quantity >= int(findByOrderQuantityGTE))

    if findByOrderQuantityLTE:
        order_query = order_query.filter(Order.order_quantity <= int(findByOrderQuantityLTE))

    if findByOrderState:
        order_query = order_query.filter(Order.order_state == findByOrderState)

    if findByOrderTagsIncludeAll:
        pass

    if findByOrderTagsIncludeAny:
        pass

    orders = order_query.all()
    return jsonify(result=(len(orders) != 0),
                   data=[o.serialize for o in orders])


@app.route('/')
def users():
    return 'working!'
