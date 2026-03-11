def find_longest_word(words):
    """
    Find longest word in a list.
    """
    if not words:
        return None
    return max(words, key=len)