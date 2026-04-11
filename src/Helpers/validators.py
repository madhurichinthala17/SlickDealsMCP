
def validate_search_item(item : str) -> tuple[bool, str]:
    """Validates the search item input.

    Args:
        item (str): The name of the item to search for.

    Returns:
        tuple[bool, str]: A tuple containing a boolean indicating if the input is valid and a string with an error message if it's not.
    """
    if not item:
        return False, "Item name cannot be empty."
    if not isinstance(item, str):
        return False, "Item name must be a string."
    if len(item) > 100:
        return False, "Item name cannot exceed 100 characters."
    if len(item) < 2:
        return False, "Item name must be at least 2 characters long."
    return True, ""