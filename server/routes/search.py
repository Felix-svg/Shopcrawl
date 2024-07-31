from flask import jsonify, request
from config import db, app
from models.search_history import SearchHistory
from models.category import Category
from models.product import Product
from utils.scrape import search_alibaba, search_amazon, search_jumia, categorize_product
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.get_saved_products import get_saved_products


@app.route("/search", methods=["GET"])
@jwt_required()
def search():
    product_name = request.args.get("q")
    current_user_id = get_jwt_identity()

    if product_name:
        # Save search history to database
        search_entry = SearchHistory(query=product_name, user_id=current_user_id)
        db.session.add(search_entry)

        def process_products(products, source):
            for product in products:
                if not product.get("product_name"):
                    continue
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
                            rating=product.get("product_rating"),
                            timestamp=datetime.utcnow(),
                            category=category,
                        )
                        db.session.add(db_product)
                except IntegrityError as e:
                    db.session.rollback()

        alibaba_data = search_alibaba(product_name)
        amazon_data = search_amazon(product_name)
        jumia_data = search_jumia(product_name)

        if not alibaba_data:
            alibaba_data = get_saved_products(product_name, "alibaba.com")

        if not amazon_data:
            amazon_data = get_saved_products(product_name, "amazon.com")

        if not jumia_data:
            jumia_data = get_saved_products(product_name, "jumia.co.ke")

        process_products(alibaba_data, "alibaba")
        process_products(amazon_data, "amazon")
        process_products(jumia_data, "jumia")

        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return jsonify({"error": "An error occurred while saving the data"}), 500

        return jsonify({"alibaba": alibaba_data, "amazon": amazon_data, "jumia": jumia_data})
    elif product_name is None or not product_name.strip():
        return jsonify({"error": "No query provided"}), 400