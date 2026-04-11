
import requests
import xml.etree.ElementTree as ET
from src.Models import Item,SearchDealsOutput
import re
from typing import List, Optional


def get_deals(item: str) -> SearchDealsOutput:
    """Searches and scrapes deal information for a given item from the SlickDeals website.

    Args:
        item (str): The name of the item to search for.

    Returns:
        SearchDealsOutput: The search result containing items and total count.
    """
    url = f"https://slickdeals.net/newsearch.php?q={item}&searchin=first&rss=1"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    deals: List[Item] = []
    for entry in root.findall(".//item"):
        title = entry.find("title").text
        link = entry.find("link").text
        price = get_deal_price(title)
        deal = Item(title=title, link=link, price=price)
        deals.append(deal)

    return SearchDealsOutput(
        result=[deal.model_dump() for deal in deals],
        total=len(deals)
    )


def get_deal_price(title: str) -> Optional[float]:
    """Extracts the price of a deal from the title of the item.

    Args:
        title (str): The title of the item.

    Returns:
        float: The extracted price.
    """

    # Regular expression to find price in the title
    price_pattern = r"\$\d+(\.\d{2})?"
    match = re.search(price_pattern, title)
    if match:
        price = match.group()
        price = float(price.replace("$", ""))
        return price
    return None

if __name__ == "__main__":
    item = input("Enter the name of the item to search for: ")
    get_deals(item)