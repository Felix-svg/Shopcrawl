import pytest

from convert_price import convert_price_to_float, adjust_price, convert_price_to_usd

# Test convert_price_to_float function
def test_convert_price_to_float_valid():
    assert convert_price_to_float("10.99") == 10.9
    assert convert_price_to_float("100,000,000.99") == 100000000.9
    assert convert_price_to_float(999.99) == 999.9
    assert convert_price_to_float(999) == 999.0
    assert convert_price_to_float(None) is None
    with pytest.raises(TypeError):
        convert_price_to_float({"price": 999.00})
    with pytest.raises(ValueError):
        convert_price_to_float("invalid price")    


def test_adjust_price():
    assert adjust_price("$10.99 - $20.99") == "$20.99"
    assert adjust_price("$5.99") == "$5.99"
    assert adjust_price(None) is None
    assert adjust_price("") is None

def test_convert_price_to_usd():
    # Test with default exchange rate
    assert convert_price_to_usd("$10.99") == "$0.08"
    assert convert_price_to_usd("$100,000,000.99") == "$710000.71"
    # Test with custom exchange rate
    assert convert_price_to_usd("$10.99", exchange_rate=0.008) == "$0.09"
    assert convert_price_to_usd("$100,000,000.99", exchange_rate=0.008) == "$800000.01"
    # Test with price range
    assert convert_price_to_usd("$10.99 - $20.99") == "$0.15"
    # Test with invalid input
    with pytest.raises(ValueError):
        convert_price_to_usd("Invalid Price")
    with pytest.raises(ValueError):
        convert_price_to_usd(None)
    # Test with empty string
    assert convert_price_to_usd("") is None