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
        return make_response({"message": "Online Community Shopping"})


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


@app.route("/search")
def search():
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


api.add_resource(Search_history, "/search_history")

api.add_resource(Home, "/")


if __name__ == "__main__":
    app.run(debug=True)
