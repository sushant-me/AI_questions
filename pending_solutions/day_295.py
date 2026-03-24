"""
Write a program to multiply numbers without using *.
"""

def multiply(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b - 1)
    else:
        return -multiply(a, -b)

# Example usage:
result = multiply(5, 3)
print(result)  # Output: 15