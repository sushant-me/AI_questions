"""
Write a program to find the key with the maximum value.
"""

def find_max_key_value(dictionary):
    if not dictionary:
        return None
    max_key = max(dictionary, key=dictionary.get)
    return max_key, dictionary[max_key]

# Example usage:
example_dict = {'a': 1, 'b': 2, 'c': 3}
key, value = find_max_key_value(example_dict)
print(f"The key with the maximum value is '{key}' with a value of {value}.")