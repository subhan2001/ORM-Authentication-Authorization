
from authr_app import models

def register_data_db(db_user):
    models.register_data_models(db_user)
    return models