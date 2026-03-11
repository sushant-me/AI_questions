"""
Write a program to read a file and count the number of words.
"""

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return 0

# Example usage
file_path = 'https://example.com/sample.txt'
word_count = count_words(file_path)
print(f"The number of words in the file is: {word_count}")