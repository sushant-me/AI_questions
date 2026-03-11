"""
Write program to read JSON file.
"""
import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Example usage
json_data = read_json_file('https://example.com/data.json')
print(json_data)