"""
Write a program to find duplicate elements in a list.
"""

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Example usage:
example_list = [1, 2, 3, 2, 4, 5, 5, 6]
print(find_duplicates(example_list))  # Output: [2, 5]