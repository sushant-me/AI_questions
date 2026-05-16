def find_missing_numbers(lst):
    """Write a program to find missing numbers in a list."""
    return list(set(range(min(lst), max(lst)+1)) - set(lst))

# Example usage:
missing_numbers = find_missing_numbers([1, 2, 4, 6, 7, 9])
print(missing_numbers)  # Output: [3, 5, 8]