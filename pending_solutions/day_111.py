"""
Write a program to handle ZeroDivisionError.
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    return result

# Example usage
numerator = 10
denominator = 0
result = divide_numbers(numerator, denominator)
if result is not None:
    print(f"The result is {result}")