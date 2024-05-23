from flask import make_response
from flask_restful import Resource

class Home(Resource):
    def get(self):
        """
        This is the root endpoint of Shopcrawl API
        ---
        tags:
            - Home
        description: Returns a welcome message.
        responses:
            200:
                description: A successful response
                examples:
                    application/json: "Shopcrawl API"
        """
        return make_response({"message": "Shopcrawl API"}, 200)