from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(16), primary_key=True)
    user_company = db.Column(db.String(128), index=True)
    user_discount_rate = db.Column(db.SmallInteger())
    orders = db.relationship('Order', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.user_company

    def __init__(self, id, user_company, user_discount_rate):
        """ Initializes the fields with entered data """
        self.id = id
        self.user_company = user_company
        self.user_discount_rate = user_discount_rate


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.String(16), primary_key=True)
    item_supplier = db.Column(db.String(128), index=True)
    item_stock_quantity = db.Column(db.Integer(), index=True)
    item_base_price = db.Column(db.Integer(), index=True)
    orders = db.relationship('Order', backref='item', lazy='dynamic')
    tags = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '<Item %r>' % self.id

    def __init__(self, id, item_supplier, item_stock_quantity, item_base_price):
        """ Initializes the fields with entered data """
        self.id = id
        self.item_supplier = item_supplier
        self.item_stock_quantity = item_stock_quantity
        self.item_base_price = item_base_price


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.String(16), primary_key=True)
    order_date_time = db.Column(db.Integer(), index=True)
    order_user_id = db.Column(db.String(16), db.ForeignKey('users.id'))
    order_item_id = db.Column(db.String(16), db.ForeignKey('items.id'))
    order_quantity = db.Column(db.Integer(), index=True)
    order_state = db.Column(db.String(128), index=True)
    tags = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '<Order %r>' % self.id

    def __init__(self, id, order_date_time, order_user_id, order_item_id,
                 order_quantty, order_state):
        """ Initializes the fields with entered data """
        self.id = id
        self.order_date_time = order_date_time
        self.order_user_id = order_user_id
        self.order_item_id = order_item_id
        self.order_quantity = order_quantty
        self.order_state = order_state

    @property
    def serialize(self):
        return {
            'orderId': self.id,
            'orderDateTime': self.order_date_time,
            'orderUserId': self.order_user_id,
            'orderItemId': self.order_item_id,
            'orderQuantity': self.order_quantity,
            'orderState': self.order_state,
            'orderTags': [tag for tag in self.tags.split(',')]
        }
