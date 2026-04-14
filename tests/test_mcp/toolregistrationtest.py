import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import pytest
from unittest.mock import MagicMock, patch
from src.Models.DataModel import Item,SearchDealsOutput


class TestToolsRegistration:

    def test_tools_registered_in_mcp(self):
        from src.Tools.mcp import mcp
        from src.Tools.pricefilter import filter_by_price
        from src.Tools.searchdeals import search_deals
        from src.Tools.latestdeals import get_latest_deals
        from src.Tools.hotdeals import get_trending_deals

        tool_names =[t.name for t in mcp._tools.values()]
        assert "search_deals" in tool_names
        assert "filter_by_price" in tool_names
        assert "get_latest_deals" in tool_names
        assert "get_trending_deals" in tool_names

    def test_all_prompts_registered(self):
        from src.Tools.mcp import mcp
        from src.Prompts.budgetshopping import budget_shopping
        from src.Prompts.findbestdeal import find_best_deal
        from src.Prompts.findlatestdeal import find_latest_deal
        prompt_names = list(mcp._prompts.keys())
        assert "find_best_deal" in prompt_names
        assert "budget_shopping" in prompt_names
        assert "find_latest_deal" in prompt_names
