"""
Write a program to find the longest word in a sentence.
"""

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
print(longest_word(sentence))  # Output: "jumps"