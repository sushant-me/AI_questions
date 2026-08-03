"""
Convert string to datetime.
"""
from datetime import datetime

def convert_string_to_datetime(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

# Example usage
date_string = "2023-10-05 14:30:00"
date_time = convert_string_to_datetime(date_string)
print(date_time)