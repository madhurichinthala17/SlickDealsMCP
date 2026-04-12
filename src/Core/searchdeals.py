from src.Services.fetcher import get_response_from_link, get_xml_response_from_link
from src.Services.parser import get_title_link_for_item , get_price_details, get_posted_details
from src.Models.DataModel import SearchDealsOutput, Item
from src.Helpers.validators import validate_search_item
from typing import List


def search_deals(xml_content : bytes) -> SearchDealsOutput:
    """
    Parses the XML content to extract deal information and returns it as a SearchDealsOutput object.
    
    Args:
        xml_content (bytes): The raw XML content containing the deal information.
    
    Returns:
        SearchDealsOutput: The search result containing items and total count.
    """
  
    title_link_list = get_title_link_for_item(xml_content)

    deals: List[Item] = []
    for title,link in title_link_list:
        responsecontent = get_response_from_link(link)
        price_details = get_price_details(responsecontent)
        posted_details = get_posted_details(responsecontent)

        deal = Item(
            title=title,
            link=link,
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