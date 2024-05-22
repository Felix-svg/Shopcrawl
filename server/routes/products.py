# server/routes/products.py

from flask import make_response
from flask_restful import Resource
from models.product import Product
from random import sample


class Products(Resource):
    def get(self):
        """
        This is an endpoint that returns all products.
        ---
        tags:
            - Products
        description: Returns products.
        responses:
            200:
                description: A successful response
                examples:
                    application/json: "Macbook Air Pro"
        """
        products = Product.query.all()
        random_products = sample(products, min(len(products), 30))

        products_data = [
            product.to_dict(rules=["-category"]) for product in random_products
        ]

        return make_response({"products": products_data}, 200)


class ProductByID(Resource):
    def get(self, id):
        """
        This is an endpoint that returns a product by its id.
        ---
        tags:
            - Product
        description: Returns a product.
        responses:
            200:
                description: A successful response
                examples:
                    application/json: "Macbook Air Pro"
            404:
                description: Product not found
        """
        product = Product.query.filter(Product.id == id).first()
        if product:
            product_dict = product.to_dict(rules=["-category"])
            return make_response({"product": product_dict}, 200)
        return make_response({"error": "Product not found"}, 404)
