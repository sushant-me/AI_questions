"""
Functions
"""

def fetch_data(url):
    """Fetch data from a given URL."""
    import requests
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_data(data):
    """Process the fetched data."""
    processed_data = [item.upper() for item in data]
    return processed_data

def main():
    url = 'https://example.com/data'
    data = fetch_data(url)
    processed_data = process_data(data)
    print(processed_data)

if __name__ == "__main__":
    main()