"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint, current_app
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
import datetime 

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({"msg": "Usuario no existe"}), 404 
    # comprobacion=current_app.bcrypt.check_password_hash(user.password, password)
    
    # if email != user.email or comprobacion == False:
    if email != user.email or password != user.password:
        return jsonify({"msg": "Bad username or password"}), 401 
    
    
    access_token = create_access_token(identity=email, expires_delta=datetime.timedelta(minutes=60))
    return jsonify(access_token=access_token) 

@api.route("/signup", methods=["POST"])
def signup():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    

    # pw_hash = current_app.bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(email=email, password=password,is_active=True)
    db.session.add(user)
    db.session.commit()

    response_body = {
        "message": "Usuario Añadido"
    }

    return jsonify(response_body), 200