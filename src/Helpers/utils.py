import re
from typing import Optional


def get_deal_price(title: str) -> Optional[float]:
    """Extracts the price of a deal from the string.

    Args:
        string (str): The string containing the price information.

    Returns:
        float: The extracted price.
    """

    # Regular expression to find price in the title
    price_pattern = r"\$\d+(\.\d{2})?"
    match = re.search(price_pattern, title)
    if match:
        price = match.group()
        price = float(price.replace("$", "").replace(",", ""))
        return price
    return None


def get_discount_percentage(discount_text: str) -> Optional[int]:
    """Extracts the discount percentage from the given text.

    Args:
        discount_text (str): The text containing the discount percentage.

    Returns:
        Optional[int]: The extracted discount percentage, or None if not found.
    """
    discount_percentage_match = re.search(r"(\d+)%", discount_text)
    if discount_percentage_match:
        return int(discount_percentage_match.group(1))
    return None


def affordability_check(price: Optional[float], max_price: float) -> bool:
    """Checks if the given price is affordable based on the maximum price.

    Args:
        price (Optional[float]): The price to check.
        max_price (float): The maximum price threshold.

    Returns:
        bool: True if the price is affordable, False otherwise.
    """
    if price is not None and price is not "N/A" and price <= max_price:
        return True
    return False