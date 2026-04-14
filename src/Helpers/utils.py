import re
from datetime import datetime, timedelta
from typing import Optional
from src.Models import RecentItem, SearchDealsOutput


def get_deal_price(title: str) -> Optional[float]:
    """Extracts the price of a deal from the string.

    Args:
        string (str): The string containing the price information.

    Returns:
        float: The extracted price.
    """

    # Regular expression to find price in the title
    price_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
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
    if price is not None and price != "N/A" and price <= max_price:
        return True
    return False


def extract_posted_date(raw_text: str) -> Optional[datetime]:
    """
    Extracts the posted date from the given raw text.
    Args:
        raw_text (str): The raw text containing the posted date information.
    
        Returns:
        datetime: The extracted posted date as a datetime object   
    """

    if not raw_text:
        return None

    now = datetime.now()

    # Extract part after "posted"
    match = re.search(r"posted\s*(.+)", raw_text, flags=re.IGNORECASE)
    date_text = match.group(1).strip() if match else raw_text.strip()

    # Handle relative dates
    if date_text.lower() == "today" or date_text.lower() == "Today":
        return now

    if date_text.lower() == "yesterday" or date_text.lower() == "Yesterday":
        return now - timedelta(days=1)

    # Handle "X hours/mins ago" (optional but useful)
    age_match = re.search(r"(\d+)\s*hour", date_text, flags=re.IGNORECASE)
    if age_match:
        return now - timedelta(hours=int(age_match.group(1)))

    age_match = re.search(r"(\d+)\s*min", date_text, flags=re.IGNORECASE)
    if age_match:
        return now - timedelta(minutes=int(age_match.group(1)))

    # Handle standard format
    try:
        return datetime.strptime(date_text, "%b %d, %Y %I:%M %p")
    except ValueError:
        return None

