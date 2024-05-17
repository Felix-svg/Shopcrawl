from convert_price import convert_price_to_float

class Product:
    def __init__(self, product_name, product_price, product_rating) -> None:
        self.product_name = product_name
        self.product_price = convert_price_to_float(product_price)
        self.product_rating = product_rating
        
   
#prompt user to input their preferences for price and rating weights
#weights represents level of importance to the user
def prompt_user_for_weights(factors):
    
    user_weights = {}
    total_weight = 0.0
    
    for factor in factors:
        weight = float(input(f"Enter the weight importance for {factor} between 0 and 1): "))
        user_weights[factor] = weight
        total_weight += weight
        
    if total_weight != 1.0:
        print("Weights must add up to 1. Adjusting weights accordingly.")
        for factor in factors: 
            user_weights[factor] /= total_weight
            
    return user_weights            

#calculate marginal benefit
def calculate_mb(product1, product2, user_weights):
    mb = 0.0
    for factor, weight in user_weights.items():
        value1 = convert_price_to_float(product1.get(factor))
        value2 = convert_price_to_float(product2.get(factor))
        
        if value1 is not None and value2 is not None:
            diff = value2 - value1
            mb += diff * weight
            
    return round(mb, 1)

#calculate cost benefit        
def calculate_cb(product1, product2):
    cb = 0.0
    if product1.get("product_price") is not None and product2.get("product_price") is not None:
        price1 = convert_price_to_float(product1.get("product_price"))
        price2 = convert_price_to_float(product2.get("product_price"))
        cb = price1 - price2
        
    return round(cb, 1)

        

#ranking algorithm to compare and rank products based on marginal benefit, cost benefit and user_weights

def calculate_score(product1, product2, user_weights):
    
    # Score calculation logic
    marginal_benefit = calculate_mb(product1, product2, user_weights)
    cost_benefit = calculate_cb(product1, product2)
    
    return marginal_benefit, cost_benefit


def rank_products(products, user_weights):
    # Ranking algorithm implementation
    ranked_products = []
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            product1 = products[i]
            product2 = products[j]
            
            marginal_benefit, cost_benefit = calculate_score(product1, product2, user_weights)
            ranked_products.append({'product1': product1, 'product2': product2, 'marginal_benefit': marginal_benefit, 'cost_benefit': cost_benefit})
            
    
    ranked_products.sort(key=lambda x: x['marginal_benefit'], reverse=True)
    return ranked_products
    
def display_ranked_products(ranked_products):
    #iterate over each item in ranked products plus its index(rank) starting from 1 instead of default 0
    for rank, product_info in enumerate(ranked_products, start=1):
        product1 = product_info['product1']
        product2 = product_info['product2']
        marginal_benefit = product_info['marginal_benefit']
        cost_benefit = product_info['cost_benefit']
        
        
        print(f"Rank {rank}:")
        print(f"Product 1 Amazon: {product1['product_name']}, Price: {product1['product_price']}, Rating: {product1['product_rating']}")
        print(f"Product 2 Alibaba: {product2['product_name']}, Price: {product2['product_price']}, Rating: {product2['product_rating']}")
        print(f"Marginal Benefit: {marginal_benefit}")
        print(f"Cost Benefit: {cost_benefit}")
        print()
 
#if mb is negative it means  there will not be a substantial benefit in purchasing more of the product
#hence they could explore other factors or products instead or adjusting their weights preferences
#positive mb indicates increasing the quantity of products would provide a greater benefit
#a -ve cb is a signal that the cost outweighs the benefit to purchasing the product