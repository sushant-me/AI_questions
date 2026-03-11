"""
Write a program using try–except–finally.
"""

try:
    response = requests.get('https://example.com')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    print("Operation attempted.")