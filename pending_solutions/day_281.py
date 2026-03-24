"""
Write a program to count trailing zeros in factorial of a number.
"""

def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

# Example usage
print(count_trailing_zeros(10))  # Output: 2