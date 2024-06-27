from flask import jsonify, request
from flask_restful import Resource
from config import db, app
from models.search_history import SearchHistory
from models.category import Category
from models.product import Product
from scrape import search_alibaba, search_amazon, search_jumia, categorize_product
from sqlalchemy.exc import IntegrityError
import logging
from datetime import datetime
import re


# # class Search(Resource):
# #     def get(self):
# #         product_name = request.args.get("q")

# #         if product_name:
# #             # Save search history to database
# #             search_entry = SearchHistory(query=product_name)
# #             db.session.add(search_entry)

# #             # Fetch and save products from Alibaba
# #             alibaba_data = search_alibaba(product_name)
# #             for product in alibaba_data:
# #                 category_name = categorize_product(product["product_name"])
# #                 category = Category.query.filter_by(name=category_name).first()
# #                 if not category:
# #                     category = Category(name=category_name)
# #                     db.session.add(category)

# #                 try:
# #                     db_product = Product.query.filter_by(name=product["product_name"]).first()
# #                     if not db_product:
# #                         db_product = Product(
# #                             name=product["product_name"],
# #                             price=product["product_price"],
# #                             image_src=product["image_src"],
# #                             source="alibaba",
# #                             rating=product["product_rating"],
# #                             category=category,
# #                         )
# #                         db.session.add(db_product)
# #                 except IntegrityError:
# #                     # Handle IntegrityError if a duplicate product is found
# #                     db.session.rollback()

# #             # Fetch and save products from Amazon
# #             amazon_data = search_amazon(product_name)
# #             for product in amazon_data:
# #                 category_name = categorize_product(product["product_name"])
# #                 category = Category.query.filter_by(name=category_name).first()
# #                 if not category:
# #                     category = Category(name=category_name)
# #                     db.session.add(category)

# #                 try:
# #                     db_product = Product.query.filter_by(name=product["product_name"]).first()
# #                     if not db_product:
# #                         db_product = Product(
# #                             name=product["product_name"],
# #                             price=product["product_price"],
# #                             image_src=product["image_src"],
# #                             source="amazon",
# #                             rating=product["product_rating"],
# #                             category=category,
# #                         )
# #                         db.session.add(db_product)
# #                 except IntegrityError:
# #                     # Handle IntegrityError if a duplicate product is found
# #                     db.session.rollback()

# #             db.session.commit()

# #             return jsonify({"alibaba": alibaba_data, "amazon": amazon_data})
# #         else:
# #             return jsonify({"error": "No query provided"}), 400


# @app.route("/search", methods=["GET"])
# def search():
#     """
#     This endpoint searches for products across multiple e-commerce platforms based on a query parameter.
#     ---
#     tags:
#         - Products
#     summary: Search for products.
#     description: Searches for products on Amazon, Alibaba, and Jumia based on the provided product name query. Saves search history and product data to the database.
#     parameters:
#         - in: query
#           name: q
#           schema:
#             type: string
#           required: true
#           description: The product name to search for.
#           example: "laptop"
#     responses:
#         200:
#             description: A successful search returning products from various platforms.
#             content:
#                 application/json:
#                     schema:
#                         type: object
#                         properties:
#                             alibaba:
#                                 type: array
#                                 items:
#                                     type: object
#                                     properties:
#                                         product_name:
#                                             type: string
#                                             example: "Laptop ABC"
#                                         product_price:
#                                             type: number
#                                             example: 500.0
#                                         image_src:
#                                             type: string
#                                             example: "http://example.com/image.jpg"
#                                         product_rating:
#                                             type: number
#                                             example: 4.5
#                                         source:
#                                             type: string
#                                             example: "alibaba"
#                             amazon:
#                                 type: array
#                                 items:
#                                     type: object
#                                     properties:
#                                         product_name:
#                                             type: string
#                                             example: "Laptop XYZ"
#                                         product_price:
#                                             type: number
#                                             example: 600.0
#                                         image_src:
#                                             type: string
#                                             example: "http://example.com/image.jpg"
#                                         product_rating:
#                                             type: number
#                                             example: 4.7
#                                         source:
#                                             type: string
#                                             example: "amazon"
#                             jumia:
#                                 type: array
#                                 items:
#                                     type: object
#                                     properties:
#                                         product_name:
#                                             type: string
#                                             example: "Laptop JKL"
#                                         product_price:
#                                             type: number
#                                             example: 550.0
#                                         image_src:
#                                             type: string
#                                             example: "http://example.com/image.jpg"
#                                         product_rating:
#                                             type: number
#                                             example: 4.6
#                                         source:
#                                             type: string
#                                             example: "jumia"
#         400:
#             description: Bad request due to missing or invalid query parameter.
#             content:
#                 application/json:
#                     schema:
#                         type: object
#                         properties:
#                             error:
#                                 type: string
#                                 example: "No query provided"
#         500:
#             description: Internal server error due to an issue saving data to the database.
#             content:
#                 application/json:
#                     schema:
#                         type: object
#                         properties:
#                             error:
#                                 type: string
#                                 example: "An error occurred while saving the data"
#     """

#     product_name = request.args.get("q")

#     if product_name:
#         # Save search history to database
#         search_entry = SearchHistory(query=product_name)
#         db.session.add(search_entry)

#         # Function to handle product data
#         def process_products(products, source):
#             for product in products:
#                 if not product.get("product_name"):
#                     # logging.error(f"Product from {source} missing name: {product}")
#                     continue
#                 category_name = categorize_product(product["product_name"])
#                 category = Category.query.filter_by(name=category_name).first()
#                 if not category:
#                     category = Category(name=category_name)
#                     db.session.add(category)

#                 try:
#                     db_product = Product.query.filter_by(
#                         name=product["product_name"]
#                     ).first()
#                     if not db_product:
#                         db_product = Product(
#                             name=product["product_name"],
#                             price=product["product_price"],
#                             image_src=product["image_src"],
#                             source=product["source"],
#                             rating=product.get(
#                                 "product_rating"
#                             ),  # Use get to avoid KeyError
#                             timestamp=datetime.utcnow(),
#                             category=category,
#                         )
#                         db.session.add(db_product)
#                 except IntegrityError as e:
#                     # logging.error(f"IntegrityError: {e}")
#                     db.session.rollback()

#         # Fetch and save products from Alibaba
#         alibaba_data = search_alibaba(product_name)
#         process_products(alibaba_data, "alibaba")

#         # Fetch and save products from Amazon
#         amazon_data = search_amazon(product_name)
#         process_products(amazon_data, "amazon")

#         # Fetch and save products from Jumia
#         jumia_data = search_jumia(product_name)
#         process_products(jumia_data, "jumia")

#         try:
#             db.session.commit()
#         except IntegrityError as e:
#             db.session.rollback()
#             logging.error(f"Commit IntegrityError: {e}")
#             return jsonify({"error": "An error occurred while saving the data"}), 500

#         return jsonify(
#             {"alibaba": alibaba_data, "amazon": amazon_data, "jumia": jumia_data}
#         )
#     elif product_name is None or not product_name.strip():
#         return jsonify({"error": "No query provided"}), 400


def get_saved_products(product_name, source_domain):
    products = Product.query.filter(
        Product.name.ilike(f"%{product_name}%"),
        Product.source.ilike(f"%{source_domain}%"),
    ).all()
    return [
        {
            "product_name": product.name,
            "product_price": product.price,
            "image_src": product.image_src,
            "product_rating": product.rating,
            "source": product.source,
        }
        for product in products
    ]


def extract_domain(url):
    match = re.search(r"https?://(?:www\.)?([^/]+)", url)
    return match.group(1) if match else None


@app.route("/search", methods=["GET"])
def search():
    """
    This endpoint searches for products across multiple e-commerce platforms based on a query parameter.
    ---
    tags:
        - Products
    summary: Search for products.
    description: Searches for products on Amazon, Alibaba, and Jumia based on the provided product name query. Saves search history and product data to the database.
    parameters:
        - in: query
          name: q
          schema:
            type: string
          required: true
          description: The product name to search for.
          example: "laptop"
    responses:
        200:
            description: A successful search returning products from various platforms.
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            alibaba:
                                type: array
                                items:
                                    type: object
                                    properties:
                                        product_name:
                                            type: string
                                            example: "Laptop ABC"
                                        product_price:
                                            type: number
                                            example: 500.0
                                        image_src:
                                            type: string
                                            example: "http://example.com/image.jpg"
                                        product_rating:
                                            type: number
                                            example: 4.5
                                        source:
                                            type: string
                                            example: "alibaba"
                            amazon:
                                type: array
                                items:
                                    type: object
                                    properties:
                                        product_name:
                                            type: string
                                            example: "Laptop XYZ"
                                        product_price:
                                            type: number
                                            example: 600.0
                                        image_src:
                                            type: string
                                            example: "http://example.com/image.jpg"
                                        product_rating:
                                            type: number
                                            example: 4.7
                                        source:
                                            type: string
                                            example: "amazon"
                            jumia:
                                type: array
                                items:
                                    type: object
                                    properties:
                                        product_name:
                                            type: string
                                            example: "Laptop JKL"
                                        product_price:
                                            type: number
                                            example: 550.0
                                        image_src:
                                            type: string
                                            example: "http://example.com/image.jpg"
                                        product_rating:
                                            type: number
                                            example: 4.6
                                        source:
                                            type: string
                                            example: "jumia"
        400:
            description: Bad request due to missing or invalid query parameter.
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            error:
                                type: string
                                example: "No query provided"
        500:
            description: Internal server error due to an issue saving data to the database.
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            error:
                                type: string
                                example: "An error occurred while saving the data"
    """
    product_name = request.args.get("q")

    if product_name:
        # Save search history to database
        search_entry = SearchHistory(query=product_name)
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
                    db_product = Product.query.filter_by(
                        name=product["product_name"]
                    ).first()
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
            logging.error(f"Commit IntegrityError: {e}")
            return jsonify({"error": "An error occurred while saving the data"}), 500

        return jsonify(
            {"alibaba": alibaba_data, "amazon": amazon_data, "jumia": jumia_data}
        )
    elif product_name is None or not product_name.strip():
        return jsonify({"error": "No query provided"}), 400
