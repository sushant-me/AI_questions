def most_frequent_char(s):
    """
    Find most frequent character.
    """
    if not s:
        return None
    
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    max_count = max(char_count.values())
    most_frequent_chars = [char for char, count in char_count.items() if count == max_count]
    
    return most_frequent_chars[0] if len(most_frequent_chars) == 1 else most_frequent_chars