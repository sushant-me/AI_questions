""" Write a program to find union of two sets. """

def find_union(set1, set2):
    return set1.union(set2)

# Example usage:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = find_union(set1, set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}