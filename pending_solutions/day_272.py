"""
Write documentation using docstrings.
"""

def fetch_data(url: str) -> dict:
    """
    Fetch data from the specified URL and return it as a dictionary.
    
    Args:
        url (str): The URL from which to fetch data.
    
    Returns:
        dict: The data fetched from the URL.
    
    Raises:
        requests.exceptions.RequestException: If an error occurs during the request.
    """
    import requests
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_data(data: dict) -> list:
    """
    Process the fetched data and return a list of relevant information.
    
    Args:
        data (dict): The data to process.
    
    Returns:
        list: A list containing relevant information from the data.
    """
    return data.get('relevant_info', [])

def main():
    """
    Main function to execute the program.
    """
    url = 'https://example.com/data'
    try:
        data = fetch_data(url)
        processed_data = process_data(data)
        print(processed_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()