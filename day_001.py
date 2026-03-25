"""
Python Programming Questions
"""

# Question 1: Write a function that takes a list of integers and returns the sum of all even numbers in the list.

def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Question 2: Create a class named 'Car' with attributes 'make', 'model', and 'year'. Add a method to display car information.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Question 3: Write a Python script that reads a file named 'data.txt' and prints the number of lines in the file.

with open('data.txt', 'r') as file:
    line_count = sum(1 for line in file)
print(f"Number of lines in data.txt: {line_count}")