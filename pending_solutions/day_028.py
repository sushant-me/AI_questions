"""
Write a program to count consonants in a string.
"""

def count_consonants(s):
    s = s.lower()
    consonants = 'bcdfghjklmnpqrstvwxyz'
    count = sum(1 for char in s if char in consonants)
    return count

# Example usage:
input_string = "Hello, World!"
print(f"Number of consonants: {count_consonants(input_string)}")