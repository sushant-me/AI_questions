""" Write a program to remove duplicates from a list. """

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)  # Output: [1, 2, 3, 4, 5]