from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SlickDealsMCP")

# Expose the underlying registry dicts for compatibility with tests.
# FastMCP uses async list_tools/list_prompts methods, so these private
# attributes provide the expected synchronous access pattern.
mcp._tools = mcp._tool_manager._tools
mcp._prompts = mcp._prompt_manager._prompts

# Import tool and prompt modules so their decorators register with the MCP instance
# when this module is imported.
from src.Tools import hotdeals, pricefilter, searchdeals, latestdeals  # noqa: F401
from src.Prompts import budgetshopping, findbestdeal, findlatestdeal  # noqa: F401