"""
Create a custom module.
"""

def fetch_data(url):
    """Fetch data from a given URL."""
    import requests
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_data(data):
    """Process data to extract specific information."""
    return {item['id']: item['name'] for item in data}