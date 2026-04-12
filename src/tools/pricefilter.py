from src.Models.DataModel import Item, PriceDetails
from src.Core.deals import get_deals
from src.Tools.mcp import mcp
from src.Helpers.utils import affordability_check


@mcp.tool()
def filter_by_price(item: str, max_price: float) -> list[Item] | str:
    """Search for deals on an item and return only those under a maximum price.

    Args:
        item (str): The item to search for.
        max_price (float): The maximum price in dollars.

    Returns:
        list[Item]: Deals under the max price, or an error message string.
    """

    # Get all deals first
    deals = get_deals(item)

    affordable_deals = []
    if not deals:
        return f"No deals found for '{item}'"

    for deal in deals.result:

        affordable = affordability_check(deal.current_price, max_price)

        if affordable:
            affordable_deals.append(deal)


    return affordable_deals
