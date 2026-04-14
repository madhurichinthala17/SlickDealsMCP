from bs4 import BeautifulSoup
from unittest.mock import MagicMock,patch

import pytest
from testdata import FAKE_RSS, FAKE_HTML

@patch('services.fetcher.requests.get')
def test_get_deals_returns_results(mock_get):
    # First call = RSS feed, second call = deal page HTML
    mock_rss = MagicMock()
    mock_rss.status_code = 200
    mock_rss.content = FAKE_RSS

    mock_html = MagicMock()
    mock_html.status_code = 200
    mock_html.content = FAKE_HTML.encode()

    mock_get.side_effect = [mock_rss, mock_html]

    from src.Core.deals import get_deals
    result = get_deals("headphones")

    assert result.total == 1
    assert result.result[0]["title"] == "Sony Headphones $249"
    assert result.result[0]["current_price"] == 249.0
    assert result.result[0]["discount_percentage"] == 29

@patch('services.fetcher.requests.get')
def test_get_deals_empty_rss(mock_get):
    mock_rss = MagicMock()
    mock_rss.status_code = 200
    mock_rss.content = b"""<?xml version="1.0"?><rss version="2.0"><channel></channel></rss>"""

    mock_get.return_value = mock_rss

    from src.Core.deals import get_deals
    result = get_deals("headphones")

    assert result.total == 0
    assert len(result.result) == 0



@patch("src.Services.fetcher.requests.get")
def test_filter_by_price_filters_correctly(mock_get):
    mock_rss = MagicMock()
    mock_rss.status_code = 200
    mock_rss.content = FAKE_RSS

    mock_html = MagicMock()
    mock_html.status_code = 200
    mock_html.content = FAKE_HTML.encode()

    mock_get.side_effect = [mock_rss, mock_html]

    from src.Tools.pricefilter import filter_by_price
    # max_price=300, deal is $249 → should appear
    result = filter_by_price("headphones", 300.0)
    assert isinstance(result, list)
    assert len(result) == 1


@patch("src.Services.fetcher.requests.get")
def test_filter_by_price_excludes_over_budget(mock_get):
    mock_rss = MagicMock()
    mock_rss.status_code = 200
    mock_rss.content = FAKE_RSS

    mock_html = MagicMock()
    mock_html.status_code = 200
    mock_html.content = FAKE_HTML.encode()

    mock_get.side_effect = [mock_rss, mock_html]

    from src.Tools.pricefilter import filter_by_price
    # max_price=200, deal is $249 → should be excluded
    result = filter_by_price("headphones", 200.0)
    assert result == []


def test_validate_rejects_empty_item():
    from src.Core.deals import get_deals
    with pytest.raises(ValueError, match="empty"):
        get_deals("")


def test_validate_rejects_single_char():
    from src.Core.deals import get_deals
    with pytest.raises(ValueError):
        get_deals("a")
