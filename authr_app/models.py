
from authr_app import db

class CreateTable(db.Model):
    # __tablename__ = "member_info"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

def register_data_models(db_user):
    db.session.add(db_user)
    db.session.commit()
