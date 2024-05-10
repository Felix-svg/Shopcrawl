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

        user = User.query.filter_by(email=email).first()

        if user:
            return {"message": "User Already Exists"}, 400

        if username and email and password:
            new_user = User(username=username, email=email)
            new_user._password_hash = password

            db.session.add(new_user)
            db.session.commit()

            access_token = create_access_token(identity=new_user.id)

            return {
                "message": "User Registration Success",
                "access_token": access_token,
            }, 201

        return make_response({"error": "422 Unprocessable Entity"}, 422)
