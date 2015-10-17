import os

# database
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

# Generate a random secret key
SECRET_KEY = os.urandom(24)

CSRF_ENABLED = True

# Disable debugging
#DEBUG = False
#HOST = "0.0.0.0"
#PORT = int(os.environ.get("PORT", 5000))
