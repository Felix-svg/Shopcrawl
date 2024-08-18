from flask import make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from datetime import timedelta
from models.user import User
from config import db
from utils.errors import missing_required_fields, server_error


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
            data = request.get_json()

            email = data.get("email")
            password = data.get("password")
            remember_me = data.get("rememberMe", False)

            if not email or not password:
                return missing_required_fields()

            user = User.query.filter(User.email == email).first()
            if user and user.check_password(password):
                expires = timedelta(days=30) if remember_me else timedelta(hours=1)
                access_token = create_access_token(
                    identity=user.id, expires_delta=expires
                )
                response = {
                    "message": "User Login Success",
                    "access_token": access_token,
                }
                return make_response(response, 200)
            else:
                return make_response({"error": "Invalid email or password"}, 401)
        except Exception as e:
            db.session.rollback()
            return server_error(e)