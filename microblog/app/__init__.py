from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager(app)

from app import views, models
