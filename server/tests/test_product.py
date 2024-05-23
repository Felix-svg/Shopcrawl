# import sys
# import os
import pytest

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from .. import convert_price
from .. import product_ranking


convert_price_to_float = convert_price.convert_price_to_float
Product = product_ranking.Product
prompt_user_for_weights = product_ranking.prompt_user_for_weights
calculate_mb = product_ranking.calculate_mb
calculate_cb = product_ranking.calculate_cb
calculate_score = product_ranking.calculate_score
rank_products = product_ranking.rank_products


def test_product_initialization():
    product = Product("Test Product", "$10.00", "4.5", "Amazon")
    assert product.product_name == "Test Product"
    assert product.product_price == 10.0
    assert product.product_rating == 4.5
    assert product.product_source == "Amazon"
    

def test_product_get_method():
    product = Product("Test Product", "$10.00", "4.5", "Amazon")
    assert product.get("product_name") == "Test Product"
    assert product.get("product_price") == 10.0
    assert product.get("product_rating") == 4.5
    assert product.get("product_source") == "Amazon"
    assert product.get("non_existent_attribute") is None
    
# Test convert_price_to_float function
def test_convert_price_to_float_valid():
    assert convert_price_to_float("10.99") == 10.99

def test_convert_price_to_float_invalid():
    with pytest.raises(ValueError):
        convert_price_to_float("invalid")

def test_convert_price_to_float_none():
    assert convert_price_to_float(None) is None
    
    
def test_prompt_user_for_weights(monkeypatch):
    #mock user input with monkeypatch
    inputs = iter(["0.3", "0.7"])  #iterator
    def mock_input(prompt):
        return next(inputs) #get next value from iterator
    
    monkeypatch.setattr('builtins.input', mock_input) #raise a stop iteration exception
    
    factors = ["Factor 1", "Factor 2"]  
    user_weights = prompt_user_for_weights(factors)
    
    assert user_weights == {"Factor 1": 0.3, "Factor 2": 0.7}  
    

def test_product_invalid_input():
    with pytest.raises(ValueError):
        Product("Invalid Product", "invalid", "invalid")
    
    
@pytest.fixture  # define sample products for testing
def sample_products(): 
    product1 = {"price": "$10.00", "rating": "4.5", "source": "Amazon"}
    product2 = {"price": "$8.50", "rating": "4.2", "source": "Alibaba"}
    product3 = {"price": "$12.00", "rating": "4.8", "source": "Jumia"}
    return product1, product2, product3
    
def test_calculate_mb(sample_products):
    product1, product2, product3 = sample_products
    
    #test case1 when all values are present
    user_weights = {"price": 0.6, "rating": 0.4} 
    expected_mb = ((8.50 - 10.00) + (12.00 - 10.00)) * 0.6 + ((4.2 - 4.5) + (4.8 - 4.5)) * 0.4 
    assert calculate_mb(product1, product2, product3, user_weights) == round(expected_mb, 1)
    
    #test case2 where there are missing values
    user_weights = {"price": 0.6, "rating": 0.4 }
    product1 = {"price": "$10.00", "rating": "4.5"}  # Missing source
    product3 = {"price": "$12.00", "rating": "4.8"}  # Missing source
    expected_mb = ((8.50 - 10.00) + (12.00 - 10.00)) * 0.6 + ((4.2 - 4.5) + (4.8 - 4.5)) * 0.4
    assert calculate_mb(product1, product2, product3, user_weights) == round(expected_mb, 1)

    # Test case 3: Missing rating for product1
    product1_no_rating = {"price": "$10.00", "source": "Amazon"}  # Missing rating
    product3 = {"price": "$12.00", "rating": "4.8", "source": "Jumia"}  # All values present for product3
    expected_mb_no_rating = ((8.50 - 10.00) + (12.00 - 10.00)) * 0.6  + (4.8 - 4.5) * 0.4
    assert calculate_mb(product1_no_rating, product2, product3, user_weights) == round(expected_mb_no_rating, 1)

    # Test case 4: Missing price for product2
    product2_no_price = {"rating": "4.2", "source": "Alibaba"}  # Missing price
    product1 = {"price": "$10.00", "rating": "4.5", "source": "Amazon"}  # All values present for product1
    expected_mb_no_price = ((12.00 - 10.00)) * 0.6 + ((4.2 - 4.5) + (4.8 - 4.5)) * 0.4
    assert calculate_mb(product1, product2_no_price, product3, user_weights) == round(expected_mb_no_price, 1)

    # Test case 5: Missing price and rating for product3
    product3_no_price_rating = {"source": "Jumia"}  # Missing price and rating
    expected_mb_no_price_rating = (8.50 - 10.00) * 0.6 + (4.2 - 4.5) * 0.4
    assert calculate_mb(product1, product2, product3_no_price_rating, user_weights) == round(expected_mb_no_price_rating, 1)

def test_calculate_cb(sample_products):
    product1, product2, product3 = sample_products

    # Test case 1: All products have prices
    expected_cb = 10.00 - 8.50 - 12.00
    assert calculate_cb(product1, product2, product3) == round(expected_cb, 1)

    # Test case 2: Missing price for product1
    product1_no_price = {"rating": "4.5", "source": "Amazon"}  # Missing price
    expected_cb_no_price1 = 12.00 - 8.50
    assert calculate_cb(product1_no_price, product2, product3) == round(expected_cb_no_price1, 1)

    # Test case 3: Missing price for product2
    product2_no_price = {"rating": "4.2", "source": "Alibaba"}  # Missing price
    expected_cb_no_price2 = 12.00 - 10.00
    assert calculate_cb(product1, product2_no_price, product3) == round(expected_cb_no_price2, 1)

    # Test case 4: Missing price for product3
    product3_no_price = {"rating": "4.8", "source": "Jumia"}  # Missing price
    expected_cb_no_price3 = 8.50 - 10.00
    assert calculate_cb(product1, product2, product3_no_price) == round(expected_cb_no_price3, 1)

    # Test case 5: Missing prices for all products
    product1_no_price = {"rating": "4.5", "source": "Amazon"}  # Missing price
    product2_no_price = {"rating": "4.2", "source": "Alibaba"}  # Missing price
    product3_no_price = {"rating": "4.8", "source": "Jumia"}  # Missing price
    assert calculate_cb(product1_no_price, product2_no_price, product3_no_price) == 0.0


def test_calculate_score(sample_products):
    product1, product2, product3 = sample_products
    user_weights = {"price": 0.6, "rating": 0.4}

    # Test case 1: All products have all attributes
    expected_mb = ((8.50 - 10.00) + (12.00 - 10.00)) * 0.6 + ((4.2 - 4.5) + (4.8 - 4.5)) * 0.4
    expected_cb = 8.50 - 10.00 - 12.00
    assert calculate_score(product1, product2, product3, user_weights) == (round(expected_mb, 1), round(expected_cb, 1))

    # Test case 2: Missing price for product1
    product1_no_price = {"rating": "4.5", "source": "Amazon"}  # Missing price
    expected_mb_no_price1 = (12.00 - 8.50) * 0.6 + (4.2 - 4.5 + 4.8 - 4.5) * 0.4
    expected_cb_no_price1 = 4.2 - 4.5 - 12.00
    assert calculate_score(product1_no_price, product2, product3, user_weights) == (round(expected_mb_no_price1, 1), round(expected_cb_no_price1, 1))

    # Test case 3: Missing price for product2
    product2_no_price = {"rating": "4.2", "source": "Alibaba"}  # Missing price
    expected_mb_no_price2 = ((12.00 - 10.00)) * 0.6 + ((4.8 - 4.5) + (4.2 - 4.5)) * 0.4
    expected_cb_no_price2 = 10.00 - 4.5 - 12.00
    assert calculate_score(product1, product2_no_price, product3, user_weights) == (round(expected_mb_no_price2, 1), round(expected_cb_no_price2, 1))

    # Test case 4: Missing price for product3
    product3_no_price = {"rating": "4.8", "source": "Jumia"}  # Missing price
    expected_mb_no_price3 = ((4.8 - 4.5) + (4.2 - 4.5)) * 0.4
    expected_cb_no_price3 = 10.00 - 8.50
    assert calculate_score(product1, product2, product3_no_price, user_weights) == (round(expected_mb_no_price3, 1), round(expected_cb_no_price3, 1))

    # Test case 5: Missing prices for all products
    product1_no_price = {"rating": "4.5", "source": "Amazon"} 
    product2_no_price = {"rating": "4.2", "source": "Alibaba"} 
    product3_no_price = {"rating": "4.8", "source": "Jumia"}
    expected_mb_no_price = (4.5 - 4.5) * 0.4  
    expected_cb_no_price = 0.0  
    assert calculate_score(product1_no_price, product2_no_price, product3_no_price, user_weights) == (round(expected_mb_no_price, 1), round(expected_cb_no_price, 1))


def test_rank_products(sample_products):
    product1, product2, product3 = sample_products
    user_weights = {"price": 0.6, "rating": 0.4}
    ranked_products = rank_products([product1, product2, product3], user_weights)

    # Check if products are ranked based on marginal benefit
    assert all(ranked_products[i]["marginal_benefit"] >= ranked_products[i + 1]["marginal_benefit"]
               for i in range(len(ranked_products) - 1))

    # Check if products are ranked correctly based on the given weights
    sorted_products = sorted(sample_products, key=lambda p: calculate_score(p, **user_weights), reverse=True)
    assert all(ranked_products[0][f"product{i+1}"] == sorted_products[i] for i in range(len(sample_products)))