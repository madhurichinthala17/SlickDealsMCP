from src.Tools import hotdeals, pricefilter, searchdeals
from src.Tools.mcp import mcp

if __name__ == "__main__":
    # Import tool modules so the @mcp.tool decorators register them before the server starts.
    mcp.run()