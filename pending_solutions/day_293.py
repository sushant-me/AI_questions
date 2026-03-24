"""
Write a program to find unique element using XOR.
"""

def find_unique_element(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Example usage
unique_element = find_unique_element([2, 3, 5, 4, 5, 3, 4])
print(unique_element)  # Output should be 2