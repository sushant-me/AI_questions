"""
Python Questions (201–300)
"""

# Example Python solution
def is_palindrome(s):
    return s == s[::-1]

# Test the function
test_string = "racecar"
result = is_palindrome(test_string)
print(result)  # Output: True