from flask import jsonify, request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from config import db
from models.search_history import SearchHistory
from models.category import Category
from models.product import Product
from scrape import search_alibaba, search_amazon, categorize_product

class Search(Resource):
    def get(self):
        product_name = request.args.get("q")

        if not product_name:
            return jsonify({"error": "No query provided"}), 400

        try:
            alibaba_data = search_alibaba(product_name)
            amazon_data = search_amazon(product_name)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        self.save_products(alibaba_data, 'alibaba')
        self.save_products(amazon_data, 'amazon')

        return jsonify({"alibaba": alibaba_data, "amazon": amazon_data})

    def save_products(self, products, source):
        for product in products:
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
                        source=source,
                        rating=product["product_rating"],
                        category=category
                    )
                    db.session.add(db_product)
            except IntegrityError:
                db.session.rollback()

        db.session.commit()


class SearchHistory(Resource):
    def get(self):
        search_histories = [history.to_dict() for history in SearchHistory.query.all()]
        return jsonify({"search_history": search_histories}), 200
