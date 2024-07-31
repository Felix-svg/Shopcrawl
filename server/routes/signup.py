
from flask import make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from config import db
from models.user import User


class Signup(Resource):
    def post(self):
        """
        This endpoint registers a new user by providing a username, email, and password.
        ---
        tags:
            - Auth
        summary: User registration
        description: Registers a new user, checks for existing username and email, hashes the password, saves the user to the database, and returns a JWT access token upon successful registration.
        requestBody:
            required: true
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            username:
                                type: string
                                description: The desired username of the new user.
                                example: "johndoe"
                            email:
                                type: string
                                description: The email address of the new user.
                                example: "johndoe@example.com"
                            password:
                                type: string
                                description: The password for the new user.
                                example: "securepassword"
        responses:
            201:
                description: User registration successful
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                message:
                                    type: string
                                    example: "User Registration Success"
                                access_token:
                                    type: string
                                    description: The JWT access token.
                                    example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
            400:
                description: Bad request due to missing details, existing username, or email
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                error:
                                    type: string
                                    example: "User details not provided"
            422:
                description: Unprocessable Entity due to invalid data
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                error:
                                    type: string
                                    example: "422 Unprocessable Entity"
        """
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
                new_user.set_password(password)

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