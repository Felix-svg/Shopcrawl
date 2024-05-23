from flask import request, jsonify
from flask_restful import Resource
from product_ranking import rank_products
from fetchrankresults import fetch_search_results

class RankProducts(Resource):
    def post(self):
        json_data = request.get_json()
        product_name = json_data.get('product_name')

        if not product_name:
            return jsonify({"error": "Product name not provided"}), 400
        
        factors = []
        if 'product_price' in json_data:
            factors.append('product_price')
            
        if 'product_rating' in json_data:
            factors.append('product_rating')
                
        price_weight = json_data.get('product_price', 1.0)  # Default weight is 1.0 if not provided
        rating_weight = json_data.get('product_rating', 1.0)  # Default weight is 1.0 if not provided
        
        user_weights = {
            'product_price': price_weight,
            'product_rating': rating_weight
        }
        
        # Perform searches
        search_results = fetch_search_results(product_name)

        if search_results:
            # rank the combined products
            ranked_products = rank_products(search_results, user_weights)

            # Return the ranked products as JSON
            return jsonify(ranked_products)
        else:
            return jsonify({"message": "No search results found for the provided product name."}), 404
