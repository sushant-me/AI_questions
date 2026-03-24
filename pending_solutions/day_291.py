"""
Write a program to calculate power using bit manipulation.
"""

def power_using_bit_manipulation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result

# Example usage:
print(power_using_bit_manipulation(2, 3))  # Output: 8