def find_missing_number(sequence):
    """ Write a program to find the missing number in a sequence. """
    n = len(sequence) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(sequence)
    return total_sum - actual_sum

# Example usage:
sequence = [1, 2, 4, 5, 6]  # Missing number is 3
missing_number = find_missing_number(sequence)
print("The missing number is:", missing_number)