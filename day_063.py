"""
Write a program to rotate a list to the left.
"""

def rotate_list_left(lst, k):
    return lst[k:] + lst[:k]

# Example usage:
# rotated_list = rotate_list_left([1, 2, 3, 4, 5], 2)
# print(rotated_list)  # Output: [3, 4, 5, 1, 2]