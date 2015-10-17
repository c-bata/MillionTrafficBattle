from flask_api import app
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from flask_api import app, db
from flask_api.models import User, Item, Order, Tag


manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    import csv

    db.drop_all()
    db.create_all()

    # user.tsv
    f = open(app.config['DATA_DIR'] + 'user.tsv')
    tsv = csv.reader(f, delimiter='\t')
    print(tsv.__next__())

    for row in tsv:
        user = User(row[0], row[1], row[2])
        db.session.add(user)
    db.session.commit()

    # item.tsv
    f = open(app.config['DATA_DIR'] + 'item.tsv')
    tsv = csv.reader(f, delimiter='\t')
    print(tsv.__next__())

    for row in tsv:
        item = Item(row[0], row[1], row[2], row[3])
        db.session.add(item)
    db.session.commit()

    # order.tsv
    f = open(app.config['DATA_DIR'] + 'order.tsv')
    tsv = csv.reader(f, delimiter='\t')
    print(tsv.__next__())

    for row in tsv:
        order = Order(row[0], row[1], row[2], row[3], row[4], row[5])
        db.session.add(order)
    db.session.commit()


@manager.command
def profile(length=25):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length])
    app.run()

if __name__ == '__main__':
    manager.run()
