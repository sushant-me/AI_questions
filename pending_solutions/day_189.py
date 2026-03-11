"""
Find shortest word in a list.
"""
def find_shortest_word(words):
    if not words:
        return None
    return min(words, key=len)

# Example usage:
words_list = ["apple", "banana", "cherry", "date"]
print(find_shortest_word(words_list))  # Output: "date"