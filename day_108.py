"""
Write a program to count words in a file.
"""

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

# Example usage
filename = 'https://example.com/sample.txt'
word_count = count_words(filename)
print(f"The number of words in the file is: {word_count}")