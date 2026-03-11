import json

# Write program to write JSON file.

data = {
    "name": "John Doe",
    "url": "https://example.com",
    "age": 30,
    "is_student": False
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)