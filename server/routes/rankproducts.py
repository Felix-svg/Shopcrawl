
from flask import request, jsonify
from flask_restful import Resource
from product_ranking import rank_products
from scrape import search_alibaba, search_amazon


class RankProducts(Resource):
    def post(self):
        json_data = request.get_json()
        product_name = json_data['product_name']
        
        factors = []
        if 'product_price' in json_data:
            factors.append('product_price')
            
        if 'product_rating' in json_data:
            factors.append('product_rating')
                
        price_weight = json_data.get('product_price')
        rating_weight = json_data.get('product_rating')
        
        user_weights = {
            'product_price': price_weight,
            'product_rating': rating_weight
        }
        
        
        # Perform searches
        amazon_products = search_amazon(product_name)
        alibaba_products = search_alibaba(product_name)

        # Combine products from both sites
        all_products = amazon_products + alibaba_products

        # Rank the combined products
        ranked_products = rank_products(all_products, user_weights)

        # Return the ranked products as JSON
        return jsonify(ranked_products)
