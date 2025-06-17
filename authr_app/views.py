
from authr_app import app, controller
from flask import request, jsonify
from authr_app.models import CreateTable
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


@app.route('/register', methods=['POST'])
def register_func():
    data = request.get_json(silent=True)
    if not data:
        return jsonify(msg="Please provide valid username and password!"), 400
    user_details = CreateTable.query.filter_by(user_name=data['username']).first()
    if not user_details:
        db_user = CreateTable(user_name=data['username'], password=data['password'])
        controller.register_data_db(db_user)
        return jsonify(msg=f"✅ User data added successfully! with {data['username']}"),200
    return jsonify(msg=f"❌ User already Exists with {data['username']}"), 400

@app.route('/login', methods=['POST'])
def login_func():
    data = request.get_json(silent=True)
    if not data:
        return jsonify(msg="Please provide valid username and password!"), 400
    user_details = CreateTable.query.filter_by(user_name=data['username'], password=data['password']).first()
    if not user_details:
        return jsonify(msg="❌ User does not Exists!"), 400
    acc_tok = create_access_token(data['username'])
    return jsonify(msg="✅ Logged-in Success!", access_token=acc_tok), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected_func():
    return jsonify(msg=f"I am from protected Route! and accessing by {get_jwt_identity()}"), 200