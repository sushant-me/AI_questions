"""
Write a program to count vowels in a string.
"""

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage
input_str = "https://example.com"
print(f"Number of vowels in '{input_str}': {count_vowels(input_str)}")