def count_set_bits(n):
    return bin(n).count('1')

# Example usage:
num = 29  # Binary: 11101
print(count_set_bits(num))  # Output: 4