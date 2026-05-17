""" Write a program to check if a list is sorted. """

def is_sorted(lst):
    return lst == sorted(lst)

# Example usage:
example_list = [1, 2, 3, 4, 5]
print(is_sorted(example_list))  # Output: True