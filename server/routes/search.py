from flask import jsonify, request
from flask_restful import Resource
from config import db
from models.search_history import SearchHistory
from models.category import Category
from models.product import Product
from scrape import search_alibaba, search_amazon, categorize_product
from sqlalchemy.exc import IntegrityError


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

                try:
                    db_product = Product.query.filter_by(name=product["product_name"]).first()
                    if not db_product:
                        db_product = Product(
                            name=product["product_name"],
                            price=product["product_price"],
                            image_src=product["image_src"],
                            source="alibaba",
                            rating=product["product_rating"],
                            category=category,
                        )
                        db.session.add(db_product)
                except IntegrityError:
                    # Handle IntegrityError if a duplicate product is found
                    db.session.rollback()

            # Fetch and save products from Amazon
            amazon_data = search_amazon(product_name)
            for product in amazon_data:
                category_name = categorize_product(product["product_name"])
                category = Category.query.filter_by(name=category_name).first()
                if not category:
                    category = Category(name=category_name)
                    db.session.add(category)

                try:
                    db_product = Product.query.filter_by(name=product["product_name"]).first()
                    if not db_product:
                        db_product = Product(
                            name=product["product_name"],
                            price=product["product_price"],
                            image_src=product["image_src"],
                            source="alibaba",
                            rating=product["product_rating"],
                            category=category,
                        )
                        db.session.add(db_product)
                except IntegrityError:
                    # Handle IntegrityError if a duplicate product is found
                    db.session.rollback()

            db.session.commit()

            return jsonify({"alibaba": alibaba_data, "amazon": amazon_data})
        else:
            return jsonify({"error": "No query provided"}), 400
