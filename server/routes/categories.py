from flask import make_response
from flask_restful import Resource
from config import db
from models.category import Category
from utils.errors import not_found, deleted, server_error


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
        try:
            categories = [
                category.to_dict(rules=["-products"]) for category in Category.query.all()
            ]
            return make_response({"categories": categories}, 200)
        except Exception as e:
            return server_error(e)


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
        try:
            category = Category.query.filter(Category.id == id).first()

            if not category:
                return not_found("Category")

            category_dict = category.to_dict(rules=["-products"])
            return make_response({"category": category_dict})
        except Exception as e:
            return server_error(e)

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
        try:
            category = Category.query.filter(Category.id == id).first()

            if not category:
                return not_found("Category")

            db.session.delete(category)
            db.session.commit()
            return deleted("Category")
        except Exception as e:
            db.session.rollback()
            return server_error(e)