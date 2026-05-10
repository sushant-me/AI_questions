"""
Write a program to find the average of numbers in a list.
"""

def find_average(numbers):
    return sum(numbers) / len(numbers)

# Example usage:
numbers = [10, 20, 30, 40, 50]
average = find_average(numbers)
print("The average is:", average)