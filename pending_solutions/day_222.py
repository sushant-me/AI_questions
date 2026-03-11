"""
Create web scraper using BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

url = 'https://example.com'
soup = web_scraper(url)

# Example usage: Extract all hyperlinks
links = [a['href'] for a in soup.find_all('a', href=True)]
print(links)