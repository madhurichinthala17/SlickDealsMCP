from src.Helpers.utils import affordability_check
import pytest

class TestAffordabilityCheck:
    @pytest.mark.parametrize("price, max_price, expected", [
        (19.99, 20.00, True),  # Price is less than max_price
        (20.00, 20.00, True),  # Price is equal to max_price
        (20.01, 20.00, False), # Price is greater than max_price
        (None, 20.00, False),   # Price is None
        ("N/A", 20.00, False),   # Price is "N/A"
        ("", 20.00, False)     # Price is an empty string
    ])
    def test_affordability_check(self, price, max_price, expected):
        assert affordability_check(price, max_price) == expected