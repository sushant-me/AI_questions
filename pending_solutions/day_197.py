"""
Write program to read CSV file.
"""

import csv

with open('https://example.com/data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)