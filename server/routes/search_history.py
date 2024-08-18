from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.search_history import SearchHistory
from models.user import User
from config import db
from sqlalchemy import inspect
from utils.errors import server_error, not_found, missing_required_fields, no_input

class SearchHistoryResource(Resource):
    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()
            current_user = User.query.get(current_user_id)

            if not current_user:
                return not_found("User")

            data = request.get_json()
            if not data:
                return no_input()
            
            query = data.get("query")

            if not query:
                return missing_required_fields()

            new_search_history = SearchHistory(query=query, user_id=current_user_id)
            db.session.add(new_search_history)
            db.session.commit()

            return {"message": "Search history created successfully", "search_history": new_search_history.to_dict()}, 201

        except Exception as e:
            return server_error(e)

    @jwt_required()
    def get(self):
        try:
            current_user_id = get_jwt_identity()

            current_user = User.query.get(current_user_id)

            if not current_user:
                return not_found("User")

            # Inspect the search_history table
            inspector = inspect(db.engine)
            columns = inspector.get_columns('search_history')

            # Use db.session.query instead of SearchHistory.query
            search_histories = db.session.query(SearchHistory).filter_by(user_id=current_user_id).all()
            return jsonify([history.to_dict(rules=['-user']) for history in search_histories])

        except Exception as e:
            return server_error(e)