import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'sample_data/')

# database
DEBUG = True
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mtb1:mtbpass1@localhost/mtb'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mtb1:mtbpass1@localhost/mtb?unix_socket=/var/lib/mysql/mysql.sock'

SLOW_DB_QUERY_TIME = 0.5

# Generate a random secret key
SECRET_KEY = os.urandom(24)

CSRF_ENABLED = True

# Disable debugging
#DEBUG = False
#HOST = "0.0.0.0"
#PORT = int(os.environ.get("PORT", 5000))
