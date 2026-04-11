
import requests
import xml.etree.ElementTree as ET
from Models import Item
import re
from typing import List, Optional


def get_deals(item: str) -> List[Item]:
    """Searches and scrapes deal information for a given item from the SlickDeals website.

    Args:
        item (str): The name of the item to search for.

    Returns:
        List[Item]: A list of Item objects containing the deal information for the item.
    """
    url = f"https://slickdeals.net/newsearch.php?q={item}&searchin=first&rss=1"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    deals: List[Item] = []
    for entry in root.findall(".//item"):
        title = entry.find("title").text
        link = entry.find("link").text
        if title is None or link is None:
            continue

        price = get_deal_price(title)
        deal = Item(title=title, link=link, price=price)
        deals.append(deal)

    return deals


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
        print(f"Price extracted from title: {price}")


if __name__ == "__main__":
    item = input("Enter the name of the item to search for: ")
    get_deals(item)