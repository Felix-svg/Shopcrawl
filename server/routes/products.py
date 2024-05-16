# server/routes/products.py

from flask import make_response
from flask_restful import Resource
from models.product import Product

class Products(Resource):
    def get(self):
        products = [product.to_dict(rules=["-category"]) for product in Product.query.all()]
        return make_response({"products": products}, 200)

class ProductByID(Resource):
    def get(self, id):
        product = Product.query.filter(Product.id == id).first()
        if product:
            product_dict = product.to_dict(rules=["-category"])
            return make_response({"product": product_dict}, 200)
        return make_response({"error": "Product not found"}, 404)
