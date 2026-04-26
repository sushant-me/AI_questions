"""
Write a program to split a list into even and odd numbers.
"""

def split_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
even, odd = split_even_odd(numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)