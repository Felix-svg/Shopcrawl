
from flask import make_response,jsonify
from flask_restful import Resource
from models.search_history import SearchHistory


class SearchHistoryResource(Resource):
    def get(self):
        search_histories = [history.to_dict() for history in SearchHistory.query.all()]
        return jsonify({"search_history": search_histories}), 200