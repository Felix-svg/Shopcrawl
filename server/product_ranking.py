from convert_price import convert_price_to_float
   
#prompt user to input their preferences for price and rating weights
def prompt_user_for_weights():
    
    price_weight = float(input("Enter the weight importance for product price(between 0 and 1): "))
    rating_weight= float(input("Enter the weight importance for product rating(between 0 and 1): "))

    #check if weights add up to 1
    total_weight = price_weight + rating_weight
    if total_weight != 1.0:
        print("Weights must add up to 1. Adjusting weights accordingly.")
        price_weight /= total_weight
        rating_weight /= total_weight
        
    user_weights = {
        'price_weight': price_weight,
        'rating_weight': rating_weight,
        'marginal_weight': 0.5, #default value
        'cost_weight': 0.5   #default value
    }
    
    return user_weights
        


def calculate_mb(product1, product2, user_weights):
    # MB calculation logic
    #weights represents level of importance to the user
    price1_str = product1.get('product_price')
    price2_str = product2.get('product_price')
    
    #check if price strings are not None
    if price1_str is not None and price2_str is not None:
        price1 = convert_price_to_float(price1_str)
        price2 = convert_price_to_float(price2_str)
        
        price_diff = price2 - price1
    else:
        price_diff = 0  #default value    
    
    # check if product ratings are not None
    rating1_str = product1.get('product_rating')
    rating2_str = product2.get('product_rating')
    if rating1_str is not None and rating2_str is not None:
        rating1 = float(rating1_str)
        rating2 = float(rating2_str)
    else:
        rating1 = 0  # default value
        rating2 = 0  # default value

    rating_diff = rating2 - rating1
    
    mb = (price_diff * user_weights['price_weight']) + (rating_diff * user_weights['rating_weight'])
    
    return mb



def calculate_cb(product1, product2):
    # CB calculation logic
    price1_str = product1.get('product_price')
    price2_str = product2.get('product_price')
    
    if price1_str is not None and price2_str is not None:
        
        price1 = convert_price_to_float(price1_str)
        price2 = convert_price_to_float(price2_str)
         
        cb = price1 - price2
    else:
        cb = 0    
    
    return cb 

#ranking algorithm to compare and rank products based on marginal_weight, cost_weight, user_weights

def calculate_score(product1, product2, user_weights):
    
    # Score calculation logic
    marginal_benefit = calculate_mb(product1, product2, user_weights)
    cost_benefit = calculate_cb(product1, product2)
    
    weighted_marginal_benefit = marginal_benefit * user_weights['marginal_weight']
    weighted_cost_benefit = cost_benefit * user_weights['cost_weight']
    
    total_score = weighted_cost_benefit + weighted_marginal_benefit
    
    #round off total score to 2 decimal places
    total_score = round(total_score, 2)
    
    return total_score


def rank_products(products, user_weights):
    # Ranking algorithm implementation
    ranked_products = []
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            product1 = products[i]
            product2 = products[j]
            
            score = calculate_score(product1, product2, user_weights)
            ranked_products.append({'product1': product1, 'product2': product2, 'score': score})
            
    
    ranked_products.sort(key=lambda x: x['score'], reverse=True)
    return ranked_products
    
def display_ranked_products(ranked_products):
    #iterate over each item in ranked products plus its index(rank) starting from 1 instead of default 0
    for rank, product_info in enumerate(ranked_products, start=1):
        product1 = product_info['product1']
        product2 = product_info['product2']
        score = product_info['score']
        
        print(f"Rank {rank}:")
        print(f"Product 1: {product1['name']}, Price: {product1['price']}, Rating: {product1['rating']}")
        print(f"Product 2: {product2['name']}, Price: {product2['price']}, Rating: {product2['rating']}")
        print(f"Score: {score}")
        print()
 