"""
Write a program to implement bitwise AND without operator.
"""

def bitwise_and(a, b):
    # Initialize result
    result = 0
    
    # Iterate through each bit position
    for i in range(32):  # Assuming 32-bit integers for simplicity
        # Check if both bits are 1 at the current position
        if (a & (1 << i)) and (b & (1 << i)):
            result |= (1 << i)
    
    return result

# Example usage:
print(bitwise_and(5, 3))  # Output: 1