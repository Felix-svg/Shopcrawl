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
            
        
        





api.add_resource(Search_history, '/search_history')

api.add_resource(Home, "/")


if __name__ == "__main__":
    app.run(debug=True)
