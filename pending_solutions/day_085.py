def is_subset(set1, set2):
    """
    Write a program to check if a set is subset of another set.
    """
    return set1.issubset(set2)

# Example usage:
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(is_subset(set_a, set_b))  # Output: True

set_c = {1, 6}
print(is_subset(set_c, set_b))  # Output: False