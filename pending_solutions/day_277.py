""" Build complete Python portfolio project. """

import requests
from bs4 import BeautifulSoup

def fetch_web_content(url):
    """Fetches the content of a web page."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_web_content(html):
    """Parses HTML content to extract information."""
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_titles(soup):
    """Extracts all titles from the parsed HTML."""
    titles = soup.find_all(['h1', 'h2', 'h3'])
    return [title.get_text() for title in titles]

def main():
    url = 'https://example.com'
    html_content = fetch_web_content(url)
    soup = parse_web_content(html_content)
    titles = extract_titles(soup)
    print("Extracted Titles:", titles)

if __name__ == "__main__":
    main()