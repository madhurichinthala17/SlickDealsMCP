from src.Tools.mcp import mcp
from src.Core.deals import get_deals, get_recent_deals

@mcp.tool()
def get_latest_deals(item: str) -> list[dict] | str:
    """Fetches the latest deals for a given item.

    Args:
        item (str): The name of the item to search for.

    Returns:
        list[dict]: A list of the latest deals for the item, or an error message

    """

    deals = get_deals(item)

    if deals.total == 0:
        return f"No deals found for '{item}'"

    return [
        {
            "title": deal.title,
            "link": str(deal.link),
            "posted_date": deal.posted_date.isoformat() if deal.posted_date else None,
        }
        for deal in get_recent_deals(deals)
    ]


