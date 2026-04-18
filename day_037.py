"""
Write a program to find the smallest element in a list.
"""

def find_smallest_element(lst):
    if not lst:
        return None
    smallest = lst[0]
    for element in lst:
        if element < smallest:
            smallest = element
    return smallest

# Example usage
example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_smallest_element(example_list))  # Output: 1