
from flask import make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models.user import User

class Login(Resource):
    def post(self):
        """
        This endpoint allows users to log in by providing their email and password.
        ---
        tags:
            - Auth
        summary: User login
        description: Validates user credentials and returns a JWT access token upon successful authentication.
        requestBody:
            required: true
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            email:
                                type: string
                                description: The user's email address.
                                example: "user@example.com"
                            password:
                                type: string
                                description: The user's password.
                                example: "password123"
        responses:
            200:
                description: User login successful
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                message:
                                    type: string
                                    example: "User Login Success"
                                access_token:
                                    type: string
                                    description: The JWT access token.
                                    example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
            400:
                description: Email or password not provided
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                error:
                                    type: string
                                    example: "Email or password not provided"
            401:
                description: Invalid username or password
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                error:
                                    type: string
                                    example: "Invalid username or password"
        """
        
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
