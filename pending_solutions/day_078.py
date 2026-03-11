"""
Write a program to sort a dictionary by values.
"""

# Python code to sort a dictionary by values
def sort_dict_by_values(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict

# Example usage
if __name__ == "__main__":
    example_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
    sorted_example_dict = sort_dict_by_values(example_dict)
    print(sorted_example_dict)