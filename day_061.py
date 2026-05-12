"""
Write a program to remove all duplicates from a list.
"""

def remove_duplicates(lst):
    return list(set(lst))

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]