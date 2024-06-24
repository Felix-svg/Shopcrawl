from convert_price import convert_price_to_float
from fetchrankresults import fetch_search_results


class Product:
    def __init__(
        self, product_name, product_price, product_rating, product_source
    ) -> None:
        self.product_name = product_name
        self.product_price = convert_price_to_float(product_price)
        self.product_rating = float(product_rating) if product_rating else None
        self.source = product_source

    def get(self, attribute):
        return getattr(self, attribute, None)


def prompt_user_for_weights(factors):
    user_weights = {}
    total_weight = 0.0

    for factor in factors:
        weight = float(
            input(f"Enter the weight importance for {factor} between 0 and 1: ")
        )
        user_weights[factor] = weight
        total_weight += weight

    if total_weight != 1.0:
        print("Weights must add up to 1. Adjusting weights accordingly.")
        for factor in user_weights:
            user_weights[factor] /= total_weight

    return user_weights


def calculate_mb(product, user_weights):
    mb = 0.0
    for factor, weight in user_weights.items():
        if factor == "product_price":
            value = convert_price_to_float(product.get(factor))
        elif factor == "product_rating":
            value = float(product.get(factor)) if product.get(factor) else None
        else:
            continue

        if value is not None:
            mb += value * weight

    return round(mb, 1)


def calculate_cb(product, user_weights):
    cb = 0.0
    price = convert_price_to_float(product.get("product_price"))
    if price is not None:
        cb += price * user_weights["product_price"]

    return round(cb, 1)

def rank_and_display_products(products, user_weights):
    ranked_products_mb = sorted(products, key=lambda x: calculate_mb(x, user_weights), reverse=False)
    ranked_products_cb = sorted(products, key=lambda x: calculate_cb(x, user_weights), reverse=True)

    ranked_products_mb_json = [
        {
            "product_name": p.product_name, 
            "product_price": p.product_price, 
            "product_rating": p.product_rating, 
            "source": p.source,
            "marginal_benefit": calculate_mb(p, user_weights)
        }
        for p in ranked_products_mb
    ]
    ranked_products_cb_json = [
        {
            "product_name": p.product_name, 
            "product_price": p.product_price, 
            "product_rating": p.product_rating, 
            "source": p.source,
            "cost_benefit": calculate_cb(p, user_weights)
        }
        for p in ranked_products_cb
    ]

    return {
        "ranked_products_mb": ranked_products_mb_json,
        "ranked_products_cb": ranked_products_cb_json
    }



def main():
    product_name = input("Enter the product name: ")

    # Fetch search results (replace with actual scraping logic)
    search_results = fetch_search_results(product_name)

    if search_results is not None:
        factors = ["product_price", "product_rating"]

        # Prompt user for weight preferences
        user_weights = prompt_user_for_weights(factors)

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

        # Rank and display the products based on mb and cb
        rank_and_display_products(products, user_weights)

    else:
        print("No search results found.")


if __name__ == "__main__":
    main()
