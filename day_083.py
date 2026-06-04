"""
Write a program to find intersection of two sets.
"""

def find_intersection(set1, set2):
    return set1.intersection(set2)

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = find_intersection(set1, set2)
print(intersection)  # Output: {4, 5}