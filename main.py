from src.Tools import hotdeals, pricefilter, searchdeals, latestdeals
from src.Tools.mcp import mcp
from src.Prompts import findbestdeal, budgetshopping

def run():
    mcp.run()

if __name__ == "__main__":
    # Import tool modules so the @mcp.tool decorators register them before the server starts.
    run()