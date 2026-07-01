"""
Exception Handling
"""

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

data = fetch_data("https://example.com")
if data:
    print("Data fetched successfully:", data)
else:
    print("Failed to fetch data.")