

def calculate_mb(ratings, mode, price, weights):
    # MB calculation logic
    #weights represents level of importance to the user
    weighted_ratings = weights['ratings'] * ratings
    weighted_mode = weights['mode'] * mode
    weighted_price = weights['price'] * price
    
    mb = weighted_ratings + weighted_mode + weighted_price
    return mb



def calculate_cb(price, delivery_cost):
    # CB calculation logic
    cb = price - delivery_cost
    return cb 

#ranking algorithm to compare and rank products based on cb and mb
#if mb is more important, you allocate more weight to mb than cb

def calculate_score(mb, cb, weights):
    # Score calculation logic
    weighted_mb = weights['mb'] * mb
    weighted_cb = weights['cb'] * cb
    
    score = weighted_mb + weighted_cb
    return score



def rank_products(products, weights):
    # Ranking algorithm implementation
    for product in products:
        mb = product['mb']
        cb = product['cb']
        score = calculate_score(mb, cb, weights)
        product['score'] = score
        
        ranked_products = sorted(products, key=lambda p: p['score'], reverse=True)
    
    return ranked_products
    
def display_ranked_products(products):
    for rank, product in enumerate(products, start=1):
        print(f"Rank {rank}: {product['name']}, Price: {product['price']}, Score: {product['score']}")
