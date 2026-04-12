from src.Services.fetcher import get_xml_response_from_link
from src.Models.DataModel import SearchDealsOutput, Item
from src.Helpers.validators import validate_search_item
from src.Core.searchdeals import search_deals
import config


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
    url = config.SLICKDEALS_RSS_URL.format(item=item)
    xml_content = get_xml_response_from_link(url)
    return search_deals(xml_content)


def get_hot_deals() -> SearchDealsOutput:
    """Fetches the current hot deals from the SlickDeals website.

    Returns:
        SearchDealsOutput: The search result containing hot deal items and total count.
    """
    url = config.SLICKDEALS_HOT_DEALS_URL
    xml_content = get_xml_response_from_link(url)
    return search_deals(xml_content)