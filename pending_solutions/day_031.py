"""
Write a program to count the frequency of characters in a string.
"""

def count_character_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example usage
example_string = "hello world"
print(count_character_frequency(example_string))