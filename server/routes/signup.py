
from flask import make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from config import db
from models.user import User


class Signup(Resource):
    def post(self):
        try:
            username = request.get_json()["username"]
            email = request.get_json()["email"]
            password = request.get_json()["password"]
        except KeyError:
            return make_response({"error": "User details not provided"}, 400)

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return make_response({"error": "Username already taken"}, 400)
        
        # Check if the email already exists
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return make_response({"error": "Email already taken"}, 400)


        if username and email and password:
            try:
                new_user = User(username=username, email=email)
                new_user.password_hash = password

                db.session.add(new_user)
                db.session.commit()

                access_token = create_access_token(identity=new_user.id)

                return make_response( {
                    "message": "User Registration Success",
                    "access_token": access_token,
                }, 201)
            except ValueError as e:
                return make_response({"error": str(e)}, 400)

        return make_response({"error": "422 Unprocessable Entity"}, 422)
