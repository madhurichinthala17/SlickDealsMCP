from src.Helpers.validators import validate_search_item
import pytest


class TestValidateSearchItem:

    @pytest.mark.parametrize("item, expected_valid, expected_message", [
        ("Laptop", True, ""),  # Valid input
        ("", False, "Item name cannot be empty."),  # Empty string
        (123, False, "Item name must be a string."),  # Non-string input
        ("A" * 101, False, "Item name cannot exceed 100 characters."),  # Exceeds max length
        ("A", False, "Item name must be at least 2 characters long.")  # Below min length
    ])
    def test_validate_search_item(self, item, expected_valid, expected_message):
        valid, message = validate_search_item(item)
        assert valid == expected_valid
        assert message == expected_message