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
    order_query = Order.query

    # senario 1
    date_time_gte = request.args.get('findByOrderDateTimeGTE')
    date_time_lte = request.args.get('findByOrderDateTimeLTE')
    order_user_id = request.args.get('findByOrderUserId')
    order_item_id = request.args.get('findByOrderItemId')
    quantity_gte = request.args.get('findByOrderQuantityGTE')
    quantity_lte = request.args.get('findByOrderQuantityLTE')
    order_state = request.args.get('findByOrderState')
    order_tags_include_all = request.args.get('findByOrderTagsIncludeAll')
    order_tags_include_any = request.args.get('findByOrderTagsIncludeAny')

    if filter(None, (date_time_gte, date_time_lte, order_user_id,
                     order_item_id, quantity_gte, quantity_lte, order_state,
                     order_tags_include_all, order_tags_include_any)):

        if date_time_gte and date_time_lte:
            order_query = order_query.filter(Order.order_date_time.between(int(date_time_gte), int(date_time_lte)))
        elif date_time_gte:
            if len(request.args) == 1:
                return jsonify(result=True, data=[])
            order_query = order_query.filter(Order.order_date_time >= int(date_time_gte))
        elif date_time_lte:
            order_query = order_query.filter(Order.order_date_time <= int(date_time_lte))

        if order_user_id:
            order_query = order_query.filter(Order.order_user_id == order_user_id)

        if order_item_id:
            order_query = order_query.filter(Order.order_item_id == order_item_id)

        if quantity_gte and quantity_lte:
            order_query = order_query.filter(Order.order_quantity.between(int(quantity_gte), int(quantity_lte)))
        elif quantity_gte:
            order_query = order_query.filter(Order.order_quantity >= int(quantity_gte))
        elif quantity_lte:
            order_query = order_query.filter(Order.order_quantity <= int(quantity_lte))

        if order_state:
            order_query = order_query.filter(Order.order_state == order_state)

        if order_tags_include_all:
            like_tags = [Order.tags.like('%' + tag + '%') for tag in order_tags_include_all.split(',')]
            order_query = order_query.filter(*like_tags)

        if order_tags_include_any:
            like_tags = [Order.tags.like('%' + tag + '%') for tag in order_tags_include_any.split(',')]
            order_query = order_query.filter(or_(*like_tags))

    # senario 2
    user_company = request.args.get('findByUserCompany')
    user_discount_rate_gte = request.args.get('findByUserDiscountRateGTE')
    user_discount_rate_lte = request.args.get('findByUserDiscountRateLTE')

    if filter(None, (user_company, user_discount_rate_lte, user_discount_rate_gte)):
        order_query = order_query.join(User)

        if user_company:
            order_query = order_query.filter(User.user_company == user_company)

        if user_discount_rate_gte and user_discount_rate_lte:
            order_query = order_query.filter(User.user_discount_rate.between(int(user_discount_rate_gte), int(user_discount_rate_lte)))
        elif user_discount_rate_gte:
            order_query = order_query.filter(User.user_discount_rate >= int(user_discount_rate_gte))
        elif user_discount_rate_lte:
            order_query = order_query.filter(User.user_discount_rate <= int(user_discount_rate_lte))

    # senario 3
    item_supplier = request.args.get('findByItemSupplier')
    item_stock_quantity_gte = request.args.get('findByItemStockQuantityGTE')
    item_stock_quantity_lte = request.args.get('findByItemStockQuantityLTE')
    item_base_price_gte = request.args.get('findByItemBasePriceGTE')
    item_base_price_lte = request.args.get('findByItemBasePriceLTE')
    item_tags_include_all = request.args.get('findByItemTagsIncludeAll')
    item_tags_include_any = request.args.get('findByItemTagsIncludeAny')

    if filter(None, (item_supplier, item_stock_quantity_gte,
                     item_stock_quantity_lte, item_base_price_gte,
                     item_stock_quantity_lte, item_tags_include_all,
                     item_tags_include_any)):
        order_query = order_query.join(Item)

        if item_supplier:
            order_query = order_query.filter(Item.item_supplier == item_supplier)

        if item_stock_quantity_gte and item_stock_quantity_lte:
            order_query = order_query.filter(Item.item_stock_quantity.between(int(item_stock_quantity_gte), int(item_stock_quantity_lte)))
        elif item_stock_quantity_gte:
            order_query = order_query.filter(Item.item_stock_quantity >= int(item_stock_quantity_gte))
        elif item_stock_quantity_lte:
            order_query = order_query.filter(Item.item_stock_quantity <= int(item_stock_quantity_lte))

        if item_base_price_gte and item_base_price_lte:
            order_query = order_query.filter(Item.item_base_price.between(int(item_base_price_gte), int(item_base_price_lte)))
        elif item_base_price_gte:
            order_query = order_query.filter(Item.item_base_price >= int(item_base_price_gte))
        elif item_base_price_lte:
            order_query = order_query.filter(Item.item_base_price <= int(item_base_price_lte))

        if item_tags_include_all:
            like_tags = [Item.tags.like('%' + tag + '%') for tag in item_tags_include_all.split(',')]
            order_query = order_query.filter(*like_tags)

        if item_tags_include_any:
            like_tags = [Item.tags.like('%' + tag + '%') for tag in item_tags_include_any.split(',')]
            order_query = order_query.filter(or_(*like_tags))

    limit = request.args.get('limit')
    if limit:
        order_query = order_query.limit(int(limit))

    orders = order_query.all()
    return jsonify(result=True, data=[o.serialize for o in orders])


@app.route('/')
def users():
    return 'working!'
