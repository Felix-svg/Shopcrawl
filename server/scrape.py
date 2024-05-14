from bs4 import BeautifulSoup
import requests
from convert_price import convert_price_to_float


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
        img_src = image["src"] if image else "No Image Found"

        title = card.find("span", {"class":"a-size-medium a-color-base a-text-normal"})
        product_name = title.text if title else "No Title Found"

        rating = card.find("i", {"class":"a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"})
        product_rating= rating.text.strip() if rating else "No Rating Found"

        price = card.find("span", {"class": "a-price-whole"})
        product_price = price.text if price else "No Price Found"

        products.append(
            {
                "image_src": img_src,
                "product_name": product_name,
                "product_price": product_price,
                "product_rating":product_rating
            }
        )

      
    products.sort(key=lambda x: convert_price_to_float(x["product_price"]))
    return products


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
        img_src = image["src"] if image else "No Image Found"

        title = card.find("h2", {"class": "search-card-e-title"})
        product_name = title.text.strip() if title else "No Title Found"

        rating = card.find("span", {"class":"search-card-e-review"})
        product_rating= rating.text.strip() if rating else "No Rating Found"

        price = card.find("div", {"class": "search-card-e-price-main"})
        product_price = price.text.strip() if price else "No Price Found"

        products.append(
            {
                "image_src": img_src,
                "product_name": product_name,
                "product_price": product_price,
                "product_rating": product_rating
            }
        )
    products.sort(key=lambda x: convert_price_to_float(x["product_price"]))
    return products


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