""" Dictionaries """

def get_dictionary_info(dictionary):
    return {
        'number_of_items': len(dictionary),
        'keys': list(dictionary.keys()),
        'values': list(dictionary.values()),
        'items': list(dictionary.items())
    }

# Example usage:
example_dict = {'a': 1, 'b': 2, 'c': 3}
info = get_dictionary_info(example_dict)
print(info)