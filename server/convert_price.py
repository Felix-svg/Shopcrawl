import re



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
        # Handle cases with multiple decimal points
        if numeric_part.count('.') > 1:
            parts = numeric_part.split('.')
            numeric_part = parts[0] + '.' + ''.join(parts[1:])
        try:
            return float(numeric_part)
        except ValueError:
            raise ValueError(f"Could not convert string to float: {price_str}")
    else:
        raise ValueError(f"Could not convert string to float: {price_str}")



def adjust_price(price_str):
    if price_str is None:
        return None
    try:
        # Split the price string by hyphen ('-') and take the second part
        upper_price_str = price_str.split("-")[-1].strip()
        return upper_price_str
    except IndexError:
        # If there's an issue with splitting the string, return None
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
