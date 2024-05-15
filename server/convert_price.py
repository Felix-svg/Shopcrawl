def convert_price_to_float(price_str):
    # Check if the price string contains a range
    if "-" in price_str:
        # Extract the numerical part of the range
        start, end = price_str.split("-")
        start = start.strip().replace("US$", "").replace(",", "")
        end = end.strip().replace("US$", "").replace(",", "")
        # Convert to float and calculate average
        start_float = float(start)
        end_float = float(end)
        return (start_float + end_float) / 2
    elif "No Price Found" in price_str:
        # Return a very high value to push it to the end of the sorted list
        return float("inf")
    else:
        # If not a range, simply convert to float
        return float(
            price_str.strip().replace("US$", "").replace(",", "").replace(".", "")
        )
