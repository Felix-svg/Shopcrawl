from flask import jsonify, make_response
from flask_restful import Resource
from config import db
from models.category import Category


class Categories(Resource):
    def get(self):
        """
        This is an endpoint that returns all product categories'
        ---
        tags:
            - Categories
        description: Returns categories.
        responses:
            200:
                description: A successful response
                examples:
                    application/json: "clothing, electronics"
        """

        categories = [
            category.to_dict(rules=["-products"]) for category in Category.query.all()
        ]
        response = make_response(jsonify({"categories": categories}), 200)
        return response


class CategoryByID(Resource):
    def get(self, id):
        """
        This is an endpoint that returns a product category by its id.
        ---
        tags:
            - Category
        description: Returns a category.
        responses:
            200:
                description: A successful response
                examples:
                    application/json: "electronics"
            404:
                description: Category not found
        """

        category = Category.query.filter(Category.id == id).first()

        if category:
            category_dict = category.to_dict(rules=["-products"])
            return make_response({"category": category_dict})
        return make_response({"error": "Category not found"}, 200)

    def delete(self, id):
        """
        This is an endpoint that deletes a product category by its id.
        ---
        tags:
            - Category
        description: Deletes a category.
        responses:
            200:
                description: Category deleted successfully
            404:
                description: Category not found
        """
        
        category = Category.query.filter(Category.id == id).first()

        if category:
            db.session.delete(category)
            db.session.commit()
            return make_response({"message": "Category deleted successfully"}, 200)
        return make_response({"error": "Category not found"}, 404)
