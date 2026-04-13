from src.Tools.mcp import mcp

@mcp.prompt()
def budget_shopping(item: str, max_price: float) -> str:
    """
    Prompt that guides LLM to find the best deals under a specified budget.
    
    Args:
        item (str): The item to search for deals on.
        max_price (float): The maximum price threshold for filtering deals.
        
    Returns:
        str: A formatted string with the best deals under the budget and analysis.
    """

    return f"""

    Search for deals on '{item}' using the filter_by_price tool with a max price of ${max_price}.
    
    Then analyze the results and:
    1. Find the best deals under the specified budget.
    2. Check if the prices seem reasonable
    3. Or else find the closest deals to the budget and analyze if they are worth considering.
    4. Be helpful and conversational in your response, and provide recommendations based on the user's budget.
    
    Format your response clearly with deal title, price, and link.
    """
