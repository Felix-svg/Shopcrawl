from flask import request, jsonify
from flask_restful import Resource
from utils.product_ranking import rank_and_display_products, Product
from utils.fetchrankresults import fetch_search_results
from flask_jwt_extended import jwt_required

class RankProducts(Resource):
    @jwt_required()
    def post(self):
        """
        This endpoint ranks products from different e-commerce platforms based on user-provided criteria.
        ---
        tags:
            - Products
        summary: Rank products based on user-defined factors.
        description: Searches for products on Amazon, Alibaba, and Jumia based on the provided product name and ranks them according to user-defined weights for price and rating.
        requestBody:
            required: true
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            product_name:
                                type: string
                                description: The name of the product to search for.
                                example: "laptop"
                            product_price:
                                type: number
                                description: The weight for the product price factor.
                                example: 0.7
                            product_rating:
                                type: number
                                description: The weight for the product rating factor.
                                example: 0.3
        responses:
            200:
                description: A list of ranked products.
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                ranked_products_mb:
                                    type: array
                                    items:
                                        type: object
                                        properties:
                                            product_name:
                                                type: string
                                                description: The name of the product.
                                                example: "Laptop XYZ"
                                            product_price:
                                                type: number
                                                description: The price of the product.
                                                example: 999.99
                                            product_rating:
                                                type: number
                                                description: The rating of the product.
                                                example: 4.5
                                            source:
                                                type: string
                                                description: The e-commerce platform where the product is found.
                                                example: "Amazon"
                                            marginal_benefit:
                                                type: number
                                                description: The calculated marginal benefit of the product.
                                                example: 7.5
                                ranked_products_cb:
                                    type: array
                                    items:
                                        type: object
                                        properties:
                                            product_name:
                                                type: string
                                                description: The name of the product.
                                                example: "Laptop XYZ"
                                            product_price:
                                                type: number
                                                description: The price of the product.
                                                example: 999.99
                                            product_rating:
                                                type: number
                                                description: The rating of the product.
                                                example: 4.5
                                            source:
                                                type: string
                                                description: The e-commerce platform where the product is found.
                                                example: "Amazon"
                                            cost_benefit:
                                                type: number
                                                description: The calculated cost benefit of the product.
                                                example: 7.5
            400:
                description: Bad request due to missing or invalid parameters.
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                error:
                                    type: string
                                    example: "Invalid request data"
        """
        
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
            # Convert search results into Product objects
            products = []
            for result in search_results:
                product = Product(
                    result.get("product_name"),
                    result.get("product_price"),
                    result.get("product_rating"),
                    result.get("source")
                )
                products.append(product)

            # Rank the combined products
            ranked_products = rank_and_display_products(products, user_weights)
            
            # Return the ranked products as JSON
            return jsonify(ranked_products)
        else:
            return jsonify({"message": "No search results found for the provided product name."}), 404