"""
Write a program to reverse a number using a loop.
"""

def reverse_number(number):
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return reversed_number

# Example usage
input_number = 12345
output_number = reverse_number(input_number)
print(f"The reversed number is: {output_number}")