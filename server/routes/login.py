from flask import make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models.user import User

class Login(Resource):
    def post(self):
        try:
            email = request.get_json()["email"]
            password = request.get_json()["password"]
        except KeyError:
            return make_response({"error": "Email or password not provided"}, 400)

        user = User.query.filter(User.email == email).first()
        if user and user.authenticate(password):
            access_token = create_access_token(identity=user.id)
            return make_response({"message": "User Login Success", "access_token": access_token}, 200)

        else:
            return make_response({"error": "Invalid username or password"}, 401)
