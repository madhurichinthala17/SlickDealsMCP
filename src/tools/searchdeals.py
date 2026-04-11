from mcp.server.fastmcp import FastMCP
from Models import Item
from Helpers.scrape import get_deals


mcp = FastMCP("SlickDealsMCP")


@mcp.tool()
def search_deals(item: str) -> list[Item]:
    """Searches for deals on the SlickDeals website for a given item.

    Args:
        item (str): The name of the item to search for

    Returns:
        list[Item]: A list of Item objects containing the deal information for the item.
    """
    deals = get_deals(item)
    return deals



