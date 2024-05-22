from bs4 import BeautifulSoup
import requests
import re
from convert_price import convert_price_to_float, adjust_price, convert_price_to_usd
# from product_ranking import (
#     rank_products,
#     display_ranked_products,
#     prompt_user_for_weights,
# )


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

        title = card.find(
            "h2", {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"}
        )
        product_name = title.text if title else None

        rating = rating = card.find("span", {"class": "a-icon-alt"})
        product_rating = None
        if rating:
            rating_text = rating.text.strip()
            # extract numerical rating using regex
            match = re.search(r"\d+\.\d+", rating_text)
            if match:
                product_rating = float(match.group())

        price = card.find("span", {"class": "a-offscreen"})
        product_price = price.text if price else None

        source = card.find("a", {"class": "a-link-normal s-no-outline"})
        product_source = f"https://www.amazon.com{source['href']}" if source else None

        products.append(
            {
                "image_src": img_src,
                "product_name": product_name,
                "product_price": product_price,
                "product_rating": product_rating,
                "source": product_source,
            }
        )

    # Filter out products with None price values
    filtered_products = [
        product for product in products if product["product_price"] is not None
    ]

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

        rating = card.find("span", {"class": "search-card-e-review"})
        product_rating = None
        if rating:
            rating_text = rating.text.strip()
            match = re.search(r"\d+\.\d+", rating_text)

            if match:
                product_rating = float(match.group())

        price = card.find("div", {"class": "search-card-e-price-main"})
        product_price = price.text.strip() if price else None

        # Adjust the price to get only the upper part of the range
        adjusted_price = adjust_price(product_price)

        source = card.find(
            "a", {"class": "search-card-e-slider__link search-card-e-slider__gallery"}
        )
        product_source = f"https:{source['href']}" if source else None

        products.append(
            {
                "image_src": img_src,
                "product_name": product_name,
                "product_price": adjusted_price,
                "product_rating": product_rating,
                "source": product_source,
            }
        )

    # Filter out products with None price values
    filtered_products = [
        product for product in products if product["product_price"] is not None
    ]

    # Sort the filtered products based on the converted price values
    filtered_products.sort(key=lambda x: convert_price_to_float(x["product_price"]))

    return filtered_products


def search_jumia(product_name):
    url = f"https://www.jumia.co.ke/catalog/?q={product_name}"
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

    product_cards = soup.find_all("article", {"class": "prd _fb col c-prd"})
    products = []

    for card in product_cards:
        image = card.find("img", {"class": "img"})
        img_src = (
            image.get("data-src") or image.get("src") or image.get("data-original")
        )

        title = card.find("h3", {"class": "name"})
        product_name = title.text.strip() if title else None

        rating = card.find("div", {"class": "stars _s"})
        product_rating = None
        if rating:
            rating_text = rating.text.strip()
            match = re.search(r"\d+\.\d+", rating_text)
            if match:
                product_rating = float(match.group())

        price = card.find("div", {"class": "prc"})
        product_price = price.text.strip() if price else None

        source = card.find("a", {"class": "core"})
        product_source = (
            f"https://www.jumia.co.ke{source['href']}" if source else None
        )  # Prepend the base URL

        if product_price is not None:
            product_price_usd = convert_price_to_usd(product_price)
            products.append(
                {
                    "image_src": img_src,
                    "product_name": product_name,
                    "product_price": product_price_usd,
                    "product_rating": product_rating,
                    "source": product_source,
                }
            )

    filtered_products = [
        product for product in products if product["product_price"] is not None
    ]
    filtered_products.sort(key=lambda x: convert_price_to_float(x["product_price"]))

    # products.sort(key=lambda x: x["product_price"])

    return filtered_products



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


# # Function to categorize products based on criteria
# def categorize_product(product_name):
#     for category, keywords in category_criteria.items():
#         for keyword in keywords:
#             if keyword.lower() in product_name.lower():
#                 return category
#     return "other"  # Default category if no match is found


def categorize_product(product_name):
    # Use a default value if product_name is None
    if product_name is None:
        product_name = ""  # or use a specific placeholder like "unknown"
    for category, keywords in category_criteria.items():
        for keyword in keywords:
            if keyword.lower() in product_name.lower():
                return category
    return "other"  # Default category if no match is found

