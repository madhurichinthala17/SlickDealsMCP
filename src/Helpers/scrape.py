import re
import requests
import xml.etree.ElementTree as ET
from src.Helpers.validators import validate_search_item
from src.Models import Item, SearchDealsOutput, PriceDetails
from bs4 import BeautifulSoup
from typing import List, Optional


def get_response_from_link(link:str) -> BeautifulSoup:
    """Fetches the HTML content of a given link and returns a BeautifulSoup object.

    Args:
        link (str): The URL to fetch.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the parsed HTML content of the page.

    """
    response = requests.get(link)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")
    

def get_deals(item: str) -> SearchDealsOutput:
    """Searches and scrapes deal information for a given item from the SlickDeals website.

    Args:
        item (str): The name of the item to search for.

    Returns:
        SearchDealsOutput: The search result containing items and total count.
    """
    is_valid, error_message = validate_search_item(item)    
    if not is_valid:
        raise ValueError(error_message)
    url = f"https://slickdeals.net/newsearch.php?q={item}&searchin=first&rss=1"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    deals: List[Item] = []
    for entry in root.findall(".//item"):
        title = entry.find("title").text
        link = entry.find("link").text
        price = get_deal_price(title)
        responsecontent = get_response_from_link(link)
        price_details = get_price_details(responsecontent)
        posted_details = get_posted_details(responsecontent)

        deal = Item(
            title=title,
            link=link,
            price=price,
            current_price=price_details.current_price if price_details else None,
            original_price=price_details.original_price if price_details else None,
            discount_percentage=price_details.discount_percentage if price_details else None,
            posted_details=posted_details,
        )
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

def get_price_details(parser: BeautifulSoup) -> Optional[PriceDetails]:
    """Extracts the price details of a deal from the deal link.

    Args:
        parser (BeautifulSoup): The BeautifulSoup object containing the parsed HTML content of the page.

    Returns:
        PriceDetails: The extracted price detail object, or None if the page has no price block.
    """

    offer_details = parser.find_all('div', class_='dealDetailsMainBlock__price')
    for i in offer_details:
        try:
            discounted_price_text = i.find('h2', class_='dealDetailsMainBlock__finalPrice').text.strip()
            discounted_price = float(discounted_price_text.replace("$", "").replace(",", ""))
        except (AttributeError, ValueError):
            discounted_price = None
        
        try:
            original_price_text = i.find('h3', class_='dealDetailsMainBlock__listPrice').text.strip()
            original_price = float(original_price_text.replace("$", "").replace(",", ""))
        except (AttributeError, ValueError):
            original_price = None
        
        try:
            discount_percentage_text = i.find('span', class_='dealDetailsMainBlock__savings').text.strip()
            discount_percentage_match = re.search(r"(\d+)%", discount_percentage_text)
            discount_percentage = int(discount_percentage_match.group(1)) if discount_percentage_match else None
        except (AttributeError, ValueError):
            discount_percentage = None

        return PriceDetails(
            current_price=discounted_price,
            original_price=original_price,
            discount_percentage=discount_percentage,
        )

    return None


def get_posted_details(parser: BeautifulSoup) -> Optional[str]:
    """Extracts the posted details of a deal from the deal link.

    Args:
        parser (BeautifulSoup): The BeautifulSoup object containing the parsed HTML content of the page.

    Returns:
        Optional[str]: The posted details of the deal or None if not found.
    """
    posted_content = parser.find('span', class_='dealDetailsMainBlock__postedInfo')
    if posted_content:
        posted_details = posted_content.get_text(strip=True)
        print(f"Posted Details: {posted_details}")
        return posted_details
    return None


if __name__ == "__main__":
    item = input("Enter the name of the item to search for: ")
    get_deals(item)