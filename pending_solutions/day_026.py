def is_palindrome(s):
    """
    Write a program to check if a string is a palindrome.
    """
    return s == s[::-1]

# Example usage:
test_string = "madam"
print(is_palindrome(test_string))  # Output: True