from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
# CORS(app)
bcrypt = Bcrypt(app)

from . import routes

