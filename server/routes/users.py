# server/routes/users.py

from flask import request
from flask_restful import Resource
from models.user import User
from config import db

class Users(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200

    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return {"error": "Missing required fields"}, 400

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return {"error": "User already exists"}, 409

        new_user = User(username=username, email=email)
        new_user.password_hash = password

        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict(), 201

class UserByID(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user is None:
            return {"error": "User not found"}, 404
        return user.to_dict(), 200

    def delete(self, id):
        user = User.query.get(id)
        if user is None:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200
