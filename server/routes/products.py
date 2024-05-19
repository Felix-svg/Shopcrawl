from flask import make_response
from flask_restful import Resource
from models.product import Product
from random import sample


# class Products(Resource):
#     def get(self):
#         products = []

#         for product in Product.query.all():
#             products.append(product.to_dict(rules=["-category"]))

#         return make_response({"products": products}, 200)

class Products(Resource):
    def get(self):
        products = Product.query.all()
        random_products = sample(products, min(len(products), 30))

        products_data = [product.to_dict(rules=["-category"]) for product in random_products]

        return make_response({"products": products_data}, 200)


class ProductByID(Resource):
    def get(self, id):
        product = Product.query.filter(Product.id == id).first()

        if product:
            product_dict = product.to_dict(rules=["-category"])
            return make_response({"product": product_dict}, 200)
        return make_response({"error": "Product not found"}, 404)
