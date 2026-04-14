from src.Helpers.utils import get_deal_price
import pytest

class TestGetDealPrice:

    def test_simple_rice(self):
        title = "Get this deal for $19.99"
        expected_price = 19.99
        assert get_deal_price(title) == expected_price

    def test_big_number(self):
        title = "Get this deal for $1,234.56"
        expected_price = 1234.56
        assert get_deal_price(title) == expected_price
    
    def test_empty_string(self):
        title = ""
        assert get_deal_price(title) is None

    def test_multiple_prices(self):
        title = "Get this deal for $19.99 on Amazon for orders above $50"
        expected_price = 19.99
        assert get_deal_price(title) == expected_price
