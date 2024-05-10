from flask import session, jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from config import db, api
from models.user import User


class Users(Resource):
    def get(self):
        try:
            users = []
            for user in User.query.all():
                users.append(user.to_dict(rules=["-_password_hash"]))
            return make_response({"users": users}, 200)
        except Exception as e:
            return make_response({"error": str(e)}, 500)



class UserByID(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if user:
            return make_response(user.to_dict(rules=["-_password_hash"]))
        return make_response({"error": "User not found"}, 404)

    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response({"message": "User deleted successfully"})
        return make_response({"Error": "User not found"})

