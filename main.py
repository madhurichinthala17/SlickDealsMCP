import os
import sys

root_dir = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(root_dir, "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

# Load local app tools before starting MCP so they register with the server.
import tools.searchdeals  # noqa: F401

# Export the server object using a standard global name for the MCP CLI.
mcp = tools.searchdeals.mcp
server = mcp
app = mcp

if __name__ == "__main__":
    mcp.run()