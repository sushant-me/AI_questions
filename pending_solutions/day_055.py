"""
Write a program to handle division by zero using exception handling.
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result

# Example usage:
num1 = 10
num2 = 0
result = divide_numbers(num1, num2)
if result is not None:
    print(f"The result is {result}")