#!/usr/bin/env python3

#remote library imports
from flask import session, jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from datetime import datetime

#local imports
from config import app, db, api

#models imports
from models.product import Product
from models.user import User
from models.category import Category
from models.search_history import SearchHistory

class Home(Resource):
    def get(self):
        return make_response({"message": "Online Community Shopping"})


class Search_history(Resource):
    def get(self):
        Search_histories = SearchHistory.query.all()
        result = []
        
        for history in Search_histories:
            result.append({
                'user_id': history.user_id,
                'product_id': history.product_id,
                'search_term': history.search_term,
                'timestamp': history.timestamp
            })
            
        return {'search_history': result}, 200
    
    def post(self):
        data = request.get_json()
        
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        search_term = data.get('search_term') 
        timestamp = datetime.now()
        
        if user_id is None or product_id is None or search_term is None:
            return {'message': 'Missing required fields'}, 400
        
        
        search_history = SearchHistory(
            user_id=user_id, 
            product_id=product_id,
            search_term=search_term, timestamp=timestamp
        )
        
        db.session.add(search_history)
        db.session.commit()

        return {'message': 'Search history added to the database'}, 200 
    
class Categories(Resource):
    def get(self):
        categories = Category.query.all()
        result = []
        
        for category in categories:
            result.append({
                'id': category.id,
                'description': category.description
            })
            
        return {'categories': result}, 200
    
class CategoryByName(Resource):
    def get(self):
        search_query = request.args.get('name')
        
        if not search_query:
            return{'message': 'Please provide a name parameter'}, 400
        
        category = Category.query.filter(Category.name.ilike(f'%{search_query}%')).first()
        
        if category:
            return{
                'name': category.name,
                'description': category.description
            }, 200
        
        else:
            return {'message': 'category not found'}, 404
        
        

api.add_resource(Home, "/")
api.add_resource(Categories, '/categories')
api.add_resource(CategoryByName, '/categories/search')
api.add_resource(Search_history, '/search_history')


if __name__ == "__main__":
    app.run(debug=True)
