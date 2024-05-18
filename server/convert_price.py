import re
def convert_price_to_float(price_str):
    if price_str is None:
        return None
    if isinstance(price_str, (int, float)):
        return float(price_str)
    if not isinstance(price_str, str):
        raise TypeError(f"Expected string or bytes-like object, got '{type(price_str).__name__}'")
    
    # Strip out any non-numeric characters except for decimal point
    numeric_part = re.search(r'[\d,.]+', price_str)
    if numeric_part:
        numeric_part = numeric_part.group().replace(',', '')
        return float(numeric_part)
    else:
        raise ValueError(f"Could not convert string to float: {price_str}")

def adjust_price(price_str):
    try:
        # Split the price string by hyphen ('-') and take the second part
        upper_price_str = price_str.split("-")[-1].strip()
        return upper_price_str
    except IndexError:
        # If there's an issue with splitting the string, return None
        return None
