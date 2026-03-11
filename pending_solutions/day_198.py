"""
Write program to write CSV file.
"""
import csv

data = [
    ['Name', 'Email', 'Phone'],
    ['John Doe', 'john@example.com', '1234567890'],
    ['Jane Smith', 'jane@example.com', '0987654321']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)