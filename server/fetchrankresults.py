import requests

def fetch_search_results(product_name):
    # Make an HTTP request to the Flask server to fetch search results
        response = requests.get("https://shopcrawl-server.onrender.com/search", params={"q": product_name})
        
        if response.status_code == 200:
            search_results = response.json()
            # Extract and combine products from search results
            all_products = search_results['jumia'] + search_results['amazon'] + search_results['alibaba']
            return all_products
         
        else:
            print("Failed to fetch search results.")
            return None
        
        
        