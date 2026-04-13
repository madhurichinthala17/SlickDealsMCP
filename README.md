# SlickDealsMCP

A Python-based MCP tool suite for scraping SlickDeals and exposing deal search functionality via an MCP server.

## Overview

`SlickDealsMCP` fetches deal information from SlickDeals using RSS search feeds and page scraping, then exposes a small set of MCP tools for:

- searching deals by item name
- fetching trending/hot deals
- filtering deals by maximum price
- returning the latest deals sorted by posted date

## Features

- `search_deals(item)` — search SlickDeals for a specific item
- `get_trending_deals()` — fetch current trending/hot deals
- `get_latest_deals(item)` — return the newest deals for an item
- `filter_by_price(item, max_price)` — list deals under a budget threshold

## Prerequisites

- Python 3.11+
- `pip`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-org/SlickDealsMCP.git
   cd SlickDealsMCP
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install fastmcp pydantic requests beautifulsoup4
   ```

## Running the project

Start the MCP server:

```bash
python main.py
```

This launches the `FastMCP` instance and registers the available tools.

## Usage

Once the server is running, use an MCP client or integration to call the registered tool methods:

- `get_trending_deals()`
- `search_deals("graphics card")`
- `get_latest_deals("headphones")`
- `filter_by_price("monitor", 200)`

## Project Structure

- `main.py` — application entrypoint
- `src/config.py` — SlickDeals RSS URL configuration
- `src/Tools/` — MCP tool definitions
- `src/Core/` — scraping and deal extraction logic
- `src/Models/` — Pydantic data models for deals and results
- `src/Services/` — network fetcher and parser utilities
- `src/Helpers/` — validators and helper utilities

## MCP Server Configuration

Add the following MCP server entry to your client or runtime configuration:

```json
{
  "mcpServers": {
    "slickdeals": {
      "command": "uvx",
      "args": ["slickdeals-mcp"]
    }
  }
}
```

## Notes

- The project relies on SlickDeals RSS feeds and page scraping, so output may vary if the target site changes.
- Use valid item search terms and ensure network connectivity for the scraper to work.


