""" Write tests using pytest. """

import pytest

def fetch_data(url):
    import requests
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def test_fetch_data():
    url = "https://example.com"
    data = fetch_data(url)
    assert "example" in data["description"], "The fetched data should contain 'example' in the description."

def test_fetch_data_raises_error_on_failure():
    with pytest.raises(requests.exceptions.HTTPError):
        fetch_data("https://example.com/nonexistent")