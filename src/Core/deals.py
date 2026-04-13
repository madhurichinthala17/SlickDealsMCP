from src.Services.fetcher import get_xml_response_from_link
from src.Models.DataModel import RecentItem, SearchDealsOutput, Item
from src.Helpers.validators import validate_search_item
from src.Core.searchdeals import search_deals
from src import config
from typing import List
from src.Helpers.utils import extract_posted_date


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


def get_recent_deals(SearchDealsOutput) -> RecentItem:
    """Sorts the deals based on their posted date and returns the list of recent items.

    Args:
        SearchDealsOutput: The search result containing items and total count.

    Returns:
        RecentItem: The sorted list of recent items based on posted date.
    """
    list_of_deals = List[RecentItem]
    for deal in SearchDealsOutput.result:
        if deal.posted_details:
            posted_date = extract_posted_date(deal.posted_details)
            recent_item = RecentItem(
                title=deal.title,
                link=deal.link,
                posted_date=posted_date
            )
            list_of_deals.append(recent_item)
    sorted_deals = sorted(list_of_deals, key=lambda x: x.posted_date, reverse=True)
    return sorted_deals