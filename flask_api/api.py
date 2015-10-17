from flask import jsonify, current_app, request
from flask.ext.sqlalchemy import get_debug_queries
from sqlalchemy import or_

from . import app, db
from .models import User, Item, Order


#@app.after_request
#def after_request(response):
#    for query in get_debug_queries():
#        if query.duration >= current_app.config['SLOW_DB_QUERY_TIME']:
#            current_app.logger.warning(
#                'Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
#                % (query.statement, query.parameters, query.duration,
#                   query.context))
#    return response


@app.route('/searchOrder')
def get_order():
    # senario 1
    date_time_gte = request.args.get('findByOrderDateTimeGTE')
    date_time_lte = request.args.get('findByOrderDateTimeLTE')
    order_user_id = request.args.get('findByOrderUserId')
    order_item_id = request.args.get('findByOrderItemId')
    quantity_gte = request.args.get('findByOrderQuantityGTE')
    quantity_lted = request.args.get('findByOrderQuantityLTE')
    order_state = request.args.get('findByOrderState')
    tags_include_all = request.args.get('findByOrderTagsIncludeAll')
    tags_include_any = request.args.get('findByOrderTagsIncludeAny')
    limit = request.args.get('limit')

    order_query = Order.query
    if date_time_gte:
        order_query = order_query.filter(Order.order_date_time >= int(date_time_gte))

    if date_time_lte:
        order_query = order_query.filter(Order.order_date_time <= int(date_time_lte))

    if order_user_id:
        order_query = order_query.filter(Order.order_user_id == order_user_id)

    if order_item_id:
        order_query = order_query.filter(Order.order_item_id == order_item_id)

    if quantity_gte:
        order_query = order_query.filter(Order.order_quantity >= int(quantity_gte))

    if quantity_lted:
        order_query = order_query.filter(Order.order_quantity <= int(quantity_lted))

    if order_state:
        order_query = order_query.filter(Order.order_state == order_state)

    if tags_include_all:
        like_tags = [Order.tags.like('%' + tag + '%') for tag in tags_include_all.split(',')]
        order_query = order_query.filter(*like_tags)

    if tags_include_any:
        like_tags = [Order.tags.like('%' + tag + '%') for tag in tags_include_any.split(',')]
        order_query = order_query.filter(or_(*like_tags))

    # senario 2
    user_company = request.args.get('findByUserCompany')
    discount_rate_gte = request.args.get('findByDisCountRateGTE')
    discount_rate_lte = request.args.get('findByDisCountRateLTE')

    #order_query = order_query.join(User)

    if user_company:
        order_query = order_query.filter(User.user_company == user_company)

    if discount_rate_gte:
        order_query = order_query.filter(User.user_discount_rate >= discount_rate_gte)

    if discount_rate_lte:
        order_query = order_query.filter(User.user_discount_rate <= discount_rate_lte)

    if limit:
        order_query = order_query.limit(int(limit))

    orders = order_query.all()
    return jsonify(result=(len(orders) != 0),
                   data=[o.serialize for o in orders])


@app.route('/')
def users():
    return 'working!'
