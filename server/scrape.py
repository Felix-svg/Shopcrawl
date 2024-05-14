from bs4 import BeautifulSoup
import requests
import re
from convert_price import convert_price_to_float
from product_ranking import rank_products, display_ranked_products, prompt_user_for_weights


def search_amazon(product_name):

    url = f"https://www.amazon.com/s?k={product_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    product_cards = soup.find_all("div", {"data-component-type": "s-search-result"})

    products = []

    for card in product_cards:

        image = card.find("img", {"class": "s-image"})
        img_src = image["src"] if image else None

        title = card.find("span", {"class":"a-size-medium a-color-base a-text-normal"})
        product_name = title.text if title else None

        rating = card.find("i", {"class":"a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"})
        product_rating= None
        if rating:
            rating_text = rating.text.strip()
            #extract numerical rating using regex
            match = re.search(r'\d+\.\d+', rating_text)
            if match:
                product_rating = float(match.group())
        
        rating_count = card.find("span", {"class": "a-size-base"})
        product_rating_count = rating_count.text.strip() if rating_count else None
        
        if product_rating:
            product_rating = f"{product_rating} ({product_rating_count})" if product_rating_count else product_rating
        else:
            product_rating  = None     

        price = card.find("span", {"class": "a-price-whole"})
        product_price = price.text if price else None

        products.append(
            {
                "image_src": img_src,
                "product_name": product_name,
                "product_price": product_price,
                "product_rating":product_rating
            }
        )

    # Filter out products with None price values
    filtered_products = [product for product in products if product["product_price"] is not None]

    # Sort the filtered products based on the converted price values
    filtered_products.sort(key=lambda x: convert_price_to_float(x["product_price"]))  
    
    return filtered_products


def search_alibaba(product_name):

    url = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText={product_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    product_cards = soup.find_all(
        "div",
        {
            "class": "fy23-search-card m-gallery-product-item-v2 J-search-card-wrapper fy23-gallery-card searchx-offer-item"
        },
    )

    products = []

    for card in product_cards:

        image = card.find("img", {"class": "search-card-e-slider__img"})
        img_src = image["src"] if image else None

        title = card.find("h2", {"class": "search-card-e-title"})
        product_name = title.text.strip() if title else None

        rating = card.find("span", {"class":"search-card-e-review"})
        product_rating= rating.text.strip() if rating else None

        price = card.find("div", {"class": "search-card-e-price-main"})
        product_price = price.text.strip() if price else None

        products.append(
            {
                "image_src": img_src,
                "product_name": product_name,
                "product_price": product_price,
                "product_rating": product_rating
            }
        )
    
    # Filter out products with None price values
    filtered_products = [product for product in products if product["product_price"] is not None]

    # Sort the filtered products based on the converted price values
    filtered_products.sort(key=lambda x: convert_price_to_float(x["product_price"]))  
    
    return filtered_products

    
def main():
    #prompt user input for product name
    product_name = input("Enter the product name: ")

    #perform searches
    amazon_products = search_amazon(product_name)
    alibaba_products = search_alibaba(product_name)

    #check if lists are empty
    if not amazon_products:
        print("No products found on Amazon.")
        
    if not alibaba_products:
        print("No products found on Alibaba.")    

    #combine products from both sites
    all_products = amazon_products + alibaba_products

    #prompt user for weight preferences
    user_weights = prompt_user_for_weights()

    #rank the combined products
    ranked_products = rank_products(all_products, user_weights)

    #display the ranked products
    display_ranked_products(ranked_products)



# Define criteria for categorization
category_criteria = {
    "electronics": ["phone", "laptop", "tablet", "camera", "television"],
    "clothing": ["shirt", "pants", "dress", "shoes", "jacket"],
    "accessories": [
        "Hats",
        "sunglasses",
        "belts",
        "scarves",
        "Keychains",
        "gloves",
        "umbrellas",
        "wallets",
    ],
    "books": [
        "literature",
        "fiction",
        "blank books",
        "children's books",
        "book",
        "calendars",
        "poetry",
        "magazines",
    ],
    "beauty": ["lip gloss", "wigs", "braids", "perfumes", "skincare"],
}


# Function to categorize products based on criteria
def categorize_product(product_name):
    for category, keywords in category_criteria.items():
        for keyword in keywords:
            if keyword.lower() in product_name.lower():
                return category
    return "other"  # Default category if no match is found

    
if __name__ == "__main__":
    main()    