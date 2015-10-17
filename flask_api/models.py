from . import db


item_tags = db.Table(
    'item_tags',
    db.Column('item_id', db.String(16), db.ForeignKey('items.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


order_tags = db.Table(
    'order_tags',
    db.Column('order_id', db.String(16), db.ForeignKey('orders.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


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

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_company': self.user_company,
            'user_discount_rate': self.user_discount_rate
        }


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.String(16), primary_key=True)
    item_supplier = db.Column(db.String(128), index=True)
    item_stock_quantity = db.Column(db.Integer(), index=True)
    item_base_price = db.Column(db.Integer(), index=True)
    orders = db.relationship('Order', backref='item', lazy='dynamic')
    tags = db.relationship('Tag', secondary=item_tags,
                           backref=db.backref('items'))

    def __repr__(self):
        return '<Item %r>' % self.id

    def __init__(self, id, item_supplier, item_stock_quantity, item_base_price):
        """ Initializes the fields with entered data """
        self.id = id
        self.item_supplier = item_supplier
        self.item_stock_quantity = item_stock_quantity
        self.item_base_price = item_base_price


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '<Tag %r>' % self.name

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_or_create(cls, tag_name):
        tag = cls.query.filter(name=tag_name).first()
        if tag:
            return tag
        else:
            return cls(tag_name)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.String(16), primary_key=True)
    order_date_time = db.Column(db.DateTime())
    order_user_id = db.Column(db.String(16), db.ForeignKey('users.id'))
    order_item_id = db.Column(db.String(16), db.ForeignKey('items.id'))
    order_quantity = db.Column(db.Integer())
    order_state = db.Column(db.String(), index=True)
    tags = db.relationship('Tag', secondary=order_tags,
                           backref=db.backref('orders'))

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
