"""
Write a program to find XOR of all elements in a list.
"""

def xor_elements(lst):
    return reduce(lambda x, y: x ^ y, lst)

# Example usage:
example_list = [1, 2, 3, 4]
result = xor_elements(example_list)
print(result)  # Output will depend on the elements in the list