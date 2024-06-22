import requests
from models.product import Product
import urllib.parse

def fetch_search_results(product_name):
    # Validate and sanitize product_name
    sanitized_product_name = urllib.parse.quote(product_name)

    try:
        # Make an HTTP request to the Flask server to fetch search results
        response = requests.get("https://shopcrawl-server.onrender.com/search", params={"q": sanitized_product_name})

        # Handle HTTP response
        response.raise_for_status()  # Raise exception for bad status codes (4xx or 5xx)

        search_results = response.json()
        jumia_results = search_results.get('jumia', [])
        amazon_results = search_results.get('amazon', [])
        alibaba_results = search_results.get('alibaba', [])

        # Combine results from all sources
        all_products = []

        # Add products from each source, ensuring uniqueness by product_name
        seen_product_names = set()
        for result_list in [jumia_results, amazon_results, alibaba_results]:
            for product in result_list:
                product_name = product.get("product_name")
                if product_name and product_name not in seen_product_names:
                    all_products.append(product)
                    seen_product_names.add(product_name)

        # Check if any source did not return results
        if not jumia_results or not amazon_results or not alibaba_results:
            # Fetch from local database and add to results, ensuring uniqueness
            local_db_results = fetch_from_database(product_name)
            if local_db_results:
                for product in local_db_results:
                    product_name = product.get("product_name")
                    if product_name and product_name not in seen_product_names:
                        all_products.append(product)
                        seen_product_names.add(product_name)

        return all_products
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch search results: {e}")
        return None

def fetch_from_database(product_name):
    """
    Fetches products from the database based on the product name.
    """
    try:
        products = Product.query.filter(Product.product_name.ilike(f"%{product_name}%")).all()
        return [
            {
                "product_name": product.product_name,
                "product_price": product.price,
                "product_rating": product.rating,
                "source": product.source
            } for product in products
        ]
    except Exception as e:
        print(f"Failed to fetch from database: {e}")
        return None