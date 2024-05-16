
from flask import request, jsonify
from flask_restful import Resource
from product_ranking import rank_products, prompt_user_for_weights
from scrape import search_alibaba, search_amazon


class RankProducts(Resource):
    def post(self):
        json_data = request.get_json()
        product_name = json_data['product_name']
       
        # Perform searches
        amazon_products = search_amazon(product_name)
        alibaba_products = search_alibaba(product_name)

        # Combine products from both sites
        all_products = amazon_products + alibaba_products

        # Prompt user for weight preferences
        user_weights = prompt_user_for_weights()

        # Rank the combined products
        ranked_products = rank_products(all_products, user_weights)

        # Return the ranked products as JSON
        return jsonify(ranked_products)
