from src.Tools.mcp import mcp


@mcp.prompt()
def find_latest_deal(item: str) -> str:
    """
    Prompt that guides LLM to find the latest deal intelligently
    Args:
        item (str): The item to search for deals on.
    
    Returns:str: A formatted string with the latest deals and analysis.
    """
    
    return f"""

    Search for deals on '{item}' using the get_latest_deals tool.
    
    Then analyze the results and:
    1. Find the most recent deal by analyzing the posted dates of the deals.
    2. Check if the price seems reasonable using get_deals to compare with other recent deals
    3.Recommend the best deals you found with your analysis and reasons.
    
    Be helpful and conversational in your response, and provide recommendations based on the latest deals you found.
    """