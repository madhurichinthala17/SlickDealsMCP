from src.Models import Item, SearchDealsOutput
from src.Core.deals import get_deals
from src.Tools.mcp import mcp


@mcp.tool()
def search_deals(item: str) -> SearchDealsOutput:
    """Searches for deals on the SlickDeals website for a given item.

    Args:
        item (str): The name of the item to search for

    Returns:
        SearchDealsOutput: The search result containing items and total count.
    """
    deals = get_deals(item)
    return deals



