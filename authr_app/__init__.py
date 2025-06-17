
from flask import Flask
from config import ConfigClass
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(ConfigClass)
db = SQLAlchemy(app)
jwt = JWTManager(app)

from authr_app.views import *
