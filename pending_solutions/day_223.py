import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    """Scrape news headlines from website."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    return headlines

# Example usage
url = 'https://example.com'
headlines = scrape_headlines(url)
print(headlines)