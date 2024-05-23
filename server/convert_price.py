import re


def clean_price_string(price_str):
    if not price_str:
        return None
    # Remove trailing periods
    cleaned_price = price_str.rstrip('.')
    # Prepend dollar sign
    return f"${cleaned_price}"

def convert_price_to_float(price_str):
    if price_str is None:
        return None
    if isinstance(price_str, (int, float)):
        return float(price_str)
    if not isinstance(price_str, str):
        raise TypeError(
            f"Expected string or bytes-like object, got '{type(price_str).__name__}'"
        )

    # Strip out any non-numeric characters except for decimal point
    numeric_part = re.search(r"[\d,.]+", price_str)
    if numeric_part:
        numeric_part = numeric_part.group().replace(",", "")
        return float(numeric_part.rstrip('.'))
    else:
        raise ValueError(f"Could not convert string to float: {price_str}")



def adjust_price(price_str):
    if not price_str:
        return None
    # Find the highest price in the range if the price is a range
    prices = re.findall(r'\d+\.?\d*', price_str.replace(",", ""))
    if prices:
        return f"${prices[-1]}"  # Prepend dollar sign to the highest price in the range
    return None


def convert_price_to_usd(price_str, exchange_rate=0.0071):
    # Adjust the price string to handle ranges
    adjusted_price_str = adjust_price(price_str)

    # Convert the adjusted price string to float
    price_ksh = convert_price_to_float(adjusted_price_str)

    # Convert the price from KSh to USD
    price_usd = price_ksh * exchange_rate

    # Format the price in USD to two decimal places with a dollar sign
    formatted_price_usd = f"${price_usd:.2f}"

    return formatted_price_usd