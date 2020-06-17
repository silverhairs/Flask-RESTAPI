from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b8fdd32a41e8b8f497e9f29a469398e4' # ⛔️ Never do this, always hide your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
marshmallow = Marshmallow(app)

from . import routes
