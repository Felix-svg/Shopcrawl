from flask import jsonify, make_response
from flask_restful import Resource
from config import db
from models.category import Category


class Categories(Resource):
    def get(self):
        categories = [
            category.to_dict(rules=["-products"]) for category in Category.query.all()
        ]
        response = make_response(jsonify({"categories": categories}), 200)
        return response


class CategoryByID(Resource):
    def get(self, id):
        category = Category.query.filter(Category.id == id).first()

        if category:
            category_dict = category.to_dict(rules=["-products"])
            return make_response({"category": category_dict})
        return make_response({"error": "Category not found"}, 200)

    def delete(self, id):
        category = Category.query.filter(Category.id == id).first()

        if category:
            db.session.delete(category)
            db.session.commit()
            return make_response({"message": "Category deleted successfully"}, 200)
        return make_response({"error": "Category not found"}, 404)