"""
Remove negative numbers from list.
"""

def remove_negatives(numbers):
    return [num for num in numbers if num >= 0]

# Example usage:
numbers = [1, -2, 3, -4, 5]
positive_numbers = remove_negatives(numbers)
print(positive_numbers)  # Output: [1, 3, 5]