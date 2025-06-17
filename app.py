
from authr_app import app, db
from authr_app.models import CreateTable

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # print("Table created!")
    app.run(debug=True)

