from src.Core.deals import get_hot_deals
from src.Models.DataModel import SearchDealsOutput
from src.Tools.mcp import mcp


@mcp.tool()
def get_trending_deals() -> SearchDealsOutput:

    """Fetches the current trending deals from SlickDeals.

    Returns:
        SearchDealsOutput: The search result containing trending deal items and total count.
    """
    return get_hot_deals()
