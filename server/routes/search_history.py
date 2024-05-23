from flask import make_response
from flask_restful import Resource
from models.search_history import SearchHistory


class Search_history(Resource):
    def get(self):
        """
        This is an endpoint that returns users search history.
        ---
        tags:
            - Search
        description: Returns search queries.
        responses:
            200:
                description: A successful response
                examples:
                    application/json: "macbook"
        """
        
        Search_histories = []

        for history in SearchHistory.query.all():
            Search_histories.append(history.to_dict())

        return make_response({"search_history": Search_histories}, 200)
