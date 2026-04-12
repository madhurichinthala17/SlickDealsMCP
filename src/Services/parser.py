import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from typing import Optional
from src.Models import PriceDetails
from src.Helpers.utils import get_deal_price, get_discount_percentage
import re

def get_title_link_for_item(content : bytes) -> list[tuple[str, str]]:
    """Extracts the title and link of each item from the XML content.

    Args:
        content (bytes): The raw XML content containing the items.
    Returns:
        list[tuple[str, str]]: A list of tuples, where each tuple contains the title and link of an item.
    """
    root = ET.fromstring(content)
    title_link_list = []
    for entry in root.findall(".//item"):
        title = entry.find("title").text
        link = entry.find("link").text
        title_link_list.append((title, link))
    return title_link_list


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
        return posted_details
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
            discounted_price = get_deal_price(discounted_price_text)
        except (AttributeError, ValueError):
            discounted_price = None
        
        try:
            original_price_text = i.find('h3', class_='dealDetailsMainBlock__listPrice').text.strip()
            original_price = get_deal_price(original_price_text)
        except (AttributeError, ValueError):
            original_price = None
        
        try:
            discount_percentage_text = i.find('span', class_='dealDetailsMainBlock__savings').text.strip()
            discount_percentage = get_discount_percentage(discount_percentage_text)
        except (AttributeError, ValueError):
            discount_percentage = None

        return PriceDetails(
            current_price=discounted_price,
            original_price=original_price,
            discount_percentage=discount_percentage,
        )

    return None