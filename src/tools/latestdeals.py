from src.Tools.mcp import mcp
from src.Core.deals import get_deals , get_recent_deals
from src.Models.DataModel import  RecentItem
from typing import List

@mcp.tool()
def get_latest_deals(item : str) -> List[RecentItem]
    """Fetches the latest deals for a given item.

    Args:
        item (str): The name of the item to search for.

    Returns:
        list[Item]: A list of the latest deals for the item, or an error message

    """

    deals = get_deals(item)

    return get_recent_deals(deals)


