from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(16), primary_key=True)
    user_company = db.Column(db.String(128), index=True)
    user_discount_rate = db.Column(db.SmallInteger())

    def __repr__(self):
        return '<User %r>' % self.user_company

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_company': self.user_company,
            'user_discount_rate': self.user_discount_rate
        }
