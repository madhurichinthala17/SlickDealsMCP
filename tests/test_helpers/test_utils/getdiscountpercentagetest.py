from src.Helpers.utils import get_discount_percentage
import pytest


class TestGetDiscountPercentage:

    def test_normal_percentage(self):
        text = "80% off"
        expected_percentage = 80.0
        assert get_discount_percentage(text) == expected_percentage

    def test_no_percentage(self):
        text = "Save with no percentage"
        assert get_discount_percentage(text) is None

    def test_empty_string(self):
        text = ""
        assert get_discount_percentage(text) is None

    def test_with_dots(self):
        text = "Get 15.5% off on this deal"
        expected_percentage = 15.5
        assert get_discount_percentage(text) == expected_percentage

    def test_extracts_100_percent(self):
        text = "Get 100% off on this deal"
        expected_percentage = 100.0
        assert get_discount_percentage(text) == expected_percentage