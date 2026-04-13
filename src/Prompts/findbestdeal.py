from src.Tools.mcp import mcp


@mcp.prompt()
def find_best_deal(item : str ) -> str:
    
    """
    Prompt that guides LLM to find the best deal intelligently
    
    Args:
        item (str): The item to search for deals on.
        
    Returns:str: A formatted string with the best deals and analysis.
    
    """

    return f"""

    Search for deals on '{item}' using the search_deals tool.
    
    Then analyze the results and:
    1. Find the lowest price by analyzing the discounts and current prices of the deals.
    2. Check if the price seems reasonable
    3. Flag any deals that look suspicious (too good to be true)
    4. Recommend the TOP 3 deals with reasons
    
    Format your response clearly with deal title, price, and link.
    """
