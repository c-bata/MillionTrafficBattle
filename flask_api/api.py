from flask import Blueprint
from .models import db

app = Blueprint('api', __name__)


@app.route('/')
def index():
    return 'Hello World'
