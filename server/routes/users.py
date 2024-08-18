from flask import make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import db, api
from models.user import User
from utils.errors import server_error, not_found, deleted, no_input, updated


class UserByID(Resource):
    @jwt_required()
    def get(self, id):
        """
        This endpoint retrieves a user by their ID.
        ---
        tags:
            - Users
        summary: Get user by ID
        description: Retrieves a user by their ID, excluding their password hash.
        parameters:
            - in: path
              name: id
              schema:
                type: integer
              required: true
              description: The ID of the user to retrieve.
              example: 1
        responses:
            200:
                description: A user object
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                id:
                                    type: integer
                                    example: 1
                                username:
                                    type: string
                                    example: "johndoe"
                                email:
                                    type: string
                                    example: "johndoe@example.com"
            404:
                description: User not found
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                error:
                                    type: string
                                    example: "User not found"
        """
        try:
            user_id = get_jwt_identity()
            if id != user_id:
                return not_found("User")

            user = User.query.get(user_id)
            if not user:
                return not_found("User")

            return make_response(
                user.to_dict(rules=["-password_hash", "-search_history"])
            )
        except Exception as e:
            return server_error(e)

    @jwt_required()
    def patch(self, id):
        """
        Updates a user by their ID.
        """
        try:
            user_id = get_jwt_identity()
            if id != user_id:
                return not_found("User")

            user = User.query.get(user_id)
            if not user:
                return not_found("User")

            data = request.get_json()
            if not data:
                return no_input()

            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if username is not None:
                user.username = username
            if email is not None:
                user.email = email
            if password is not None:
                user.set_password(password)

            db.session.commit()
            return updated("User")
        except Exception as e:
            db.session.rollback()
            return server_error(e)

    @jwt_required()
    def delete(self, id):
        """
        This endpoint deletes a user by their ID.
        ---
        tags:
            - Users
        summary: Delete user by ID
        description: Deletes a user by their ID.
        parameters:
            - in: path
              name: id
              schema:
                type: integer
              required: true
              description: The ID of the user to delete.
              example: 1
        responses:
            200:
                description: User deleted successfully
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                message:
                                    type: string
                                    example: "User deleted successfully"
            404:
                description: User not found
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                error:
                                    type: string
                                    example: "User not found"
        """
        try:
            user_id = get_jwt_identity()
            if id != user_id:
                return not_found("User")

            user = User.query.get(user_id)
            if not user:
                return not_found("User")

            db.session.delete(user)
            db.session.commit()
            return deleted("User")
        except Exception as e:
            return server_error(e)
