def is_palindrome(number):
    """Write a program to check if a number is a palindrome without converting to string."""
    
    # Initialize variables for the original number and its reverse
    original_number = number
    reversed_number = 0
    
    # Reverse the number without using string conversion
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    
    # Check if the original number is equal to its reverse
    return original_number == reversed_number

# Example usage
print(is_palindrome(12321))  # Output: True
print(is_palindrome(12345))  # Output: False