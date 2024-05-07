from config import app, db, api
from flask import session, jsonify, make_response, request
from flask_restful import Resource
from models.product import Product
from models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt


class Home(Resource):
    def get(self):
        return make_response({"message": "Online Community Shopping"})


api.add_resource(Home, "/")


if __name__ == "__main__":
    app.run(debug=True)
