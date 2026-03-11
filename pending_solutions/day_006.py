"""
Write a program to check if a number is even or odd.
"""

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Example usage
check_even_odd(4)  # Output: 4 is even.
check_even_odd(7)  # Output: 7 is odd.