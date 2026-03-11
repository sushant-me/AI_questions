"""
Write a program to count digits in a number.
"""

def count_digits(number):
    return len(str(abs(number)))

# Example usage:
number = 12345
print(f"The number {number} has {count_digits(number)} digits.")