from src import config
from bs4 import BeautifulSoup
import requests


def get_response_from_link(link:str) -> BeautifulSoup:
    """Fetches the HTML content of a given link and returns a BeautifulSoup object.

    Args:
        link (str): The URL to fetch.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the parsed HTML content of the page.

    """
    response = requests.get(link)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")
    

def get_xml_response_from_link(url : str) -> bytes:
    """Fetches the XML content of a given link

    Args:
        url (str): The URL to fetch.

    Returns:
        bytes: The raw XML content of the page.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")