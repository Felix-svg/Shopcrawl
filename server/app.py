#!/usr/bin/env python3

# remote library imports
from flask import session, jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from datetime import datetime

# local imports
from config import app, db, api
from scrape import search_alibaba, search_amazon, categorize_product

# models imports
from models.product import Product
from models.user import User
from models.search_history import SearchHistory
from models.category import Category


class Home(Resource):
    def get(self):
        return make_response({"message": "Shopcrawl API"})


api.add_resource(Home, "/")


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
            new_user.password_hash = password

            db.session.add(new_user)
            db.session.commit()

            access_token = create_access_token(identity=new_user.id)

            return {
                "message": "User Registration Success",
                "access_token": access_token,
            }, 201

        return make_response({"error": "422 Unprocessable Entity"}, 422)


api.add_resource(Signup, "/signup")


class Login(Resource):
    def post(self):
        try:
            email = request.get_json()["email"]
            password = request.get_json()["password"]
        except KeyError:
            return make_response({"error": "Email or password not provided"}, 400)

        user = User.query.filter(User.email == email).first()
        if user and user.authenticate(password):
            access_token = create_access_token(identity=user.id)
            return {"message": "User Login Success", "access_token": access_token}, 200

        else:
            return make_response({"error": "Invalid username or password"}, 401)


api.add_resource(Login, "/login")


class Users(Resource):
    def get(self):
        try:
            users = []
            for user in User.query.all():
                users.append(user.to_dict(rules=["-blogs", "-_password_hash"]))
            return make_response({"users": users}, 200)
        except Exception as e:
            return make_response({"error": str(e)}, 500)


api.add_resource(Users, "/users")


class UserByID(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if user:
            return make_response(user.to_dict())
        return make_response({"error": "User not found"})

    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response({"message": "User deleted successfully"})
        return make_response({"Error": "User not found"})


api.add_resource(UserByID, "/user/<int:id>")


class Search_history(Resource):
    def get(self):
        Search_histories = SearchHistory.query.all()
        result = []

        for history in Search_histories:
            result.append(
                {
                    "user_id": history.user_id,
                    "product_id": history.product_id,
                    "search_term": history.search_term,
                    "timestamp": history.timestamp,
                }
            )

        return {"search_history": result}, 200

    # def post(self):
    #     data = request.get_json()

    #     user_id = data.get("user_id")
    #     product_id = data.get("product_id")
    #     search_term = data.get("search_term")
    #     timestamp = datetime.now()

    #     if user_id is None or product_id is None or search_term is None:
    #         return {"message": "Missing required fields"}, 400

    #     search_history = SearchHistory(
    #         user_id=user_id,
    #         product_id=product_id,
    #         search_term=search_term,
    #         timestamp=timestamp,
    #     )

    #     db.session.add(search_history)
    #     db.session.commit()

    #     return {"message": "Search history added to the database"}, 200


class Search(Resource):
    def get(self):
        product_name = request.args.get("q")

        if product_name:
            # Save search history to database
            search_entry = SearchHistory(query=product_name)
            db.session.add(search_entry)

            # Fetch and save products from Alibaba
            alibaba_data = search_alibaba(product_name)
            for product in alibaba_data:
                category_name = categorize_product(product["product_name"])
                category = Category.query.filter_by(name=category_name).first()
                if not category:
                    category = Category(name=category_name)
                    db.session.add(category)

                db_product = Product(
                    name=product["product_name"],
                    price=product["product_price"],
                    image_src=product["image_src"],
                    source="alibaba",
                    category=category,
                )
                db.session.add(db_product)

            # Fetch and save products from Amazon
            amazon_data = search_amazon(product_name)
            for product in amazon_data:
                category_name = categorize_product(product["product_name"])
                category = Category.query.filter_by(name=category_name).first()
                if not category:
                    category = Category(name=category_name)
                    db.session.add(category)

                db_product = Product(
                    name=product["product_name"],
                    price=product["product_price"],
                    image_src=product["image_src"],
                    source="amazon",
                    category=category,
                )
                db.session.add(db_product)

            db.session.commit()

            return jsonify({"alibaba": alibaba_data, "amazon": amazon_data})
        else:
            return jsonify({"error": "No query provided"}), 400


api.add_resource(Search, "/search")


if __name__ == "__main__":
    app.run(debug=True)
