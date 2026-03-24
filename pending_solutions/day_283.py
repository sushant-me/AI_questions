"""
Write a program to find the binary representation of a number.
"""

def decimal_to_binary(decimal_number):
    return bin(decimal_number).replace("0b", "")

# Example usage:
print(decimal_to_binary(10))  # Output: 1010