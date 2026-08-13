"""
Write a program using list comprehension.
"""

# Define a function to create a list of squares of even numbers from 1 to 10
def even_squares():
    return [x**2 for x in range(1, 11) if x % 2 == 0]

# Call the function and print the result
print(even_squares())