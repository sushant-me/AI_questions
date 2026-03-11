"""
Mock functions for testing.
"""

def mock_function():
    """ Mock function for testing. """
    return "Mocked response"

def mock_api_call(url):
    """ Mock function to simulate an API call. """
    return {"url": url, "status": "200 OK", "data": "Mocked data"}