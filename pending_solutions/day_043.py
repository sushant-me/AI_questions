"""
Write a program to reverse a list.
"""

def reverse_list(input_list):
    return input_list[::-1]

# Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)  # Output: [5, 4, 3, 2, 1]