
from datetime import timedelta

class ConfigClass:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin2025@localhost/project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=2)
    JWT_SECRET_KEY = 'secret key'

