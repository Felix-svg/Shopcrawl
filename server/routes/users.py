from flask import session, jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from config import db, api
from models.user import User


class Users(Resource):
    def get(self):
        """
        This endpoint retrieves a list of all users.
        ---
        tags:
            - Users
        summary: Get all users
        description: Retrieves a list of all users in the system, excluding their password hashes.
        responses:
            200:
                description: A list of users
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                users:
                                    type: array
                                    items:
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
            500:
                description: Internal server error
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                error:
                                    type: string
                                    example: "An error occurred while retrieving the users"
        """
        
        try:
            users = []
            for user in User.query.all():
                users.append(user.to_dict(rules=["-_password_hash"]))
            return make_response({"users": users}, 200)
        except Exception as e:
            return make_response({"error": str(e)}, 500)



class UserByID(Resource):
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

        user = User.query.filter(User.id == id).first()

        if user:
            return make_response(user.to_dict(rules=["-_password_hash"]))
        return make_response({"error": "User not found"}, 404)

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
        user = User.query.filter(User.id == id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response({"message": "User deleted successfully"})
        return make_response({"Error": "User not found"})

