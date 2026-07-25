"""
Modules & Packages
"""

# Importing a module
import math

# Using a function from a module
result = math.sqrt(16)
print(result)

# Importing specific functions from a module
from datetime import datetime

# Using a specific function from a module
current_time = datetime.now()
print(current_time)

# Importing a package
import requests

# Using a function from a package
response = requests.get('https://example.com')
print(response.text)

# Importing a specific function from a package
from json import loads

# Using a specific function from a package
json_data = '{"name": "John", "age": 30}'
data = loads(json_data)
print(data)