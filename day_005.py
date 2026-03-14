"""
Write a program to swap two variables without using a third variable.
"""

def swap_variables(a, b):
    a, b = b, a
    return a, b

# Example usage:
x = 5
y = 10
x, y = swap_variables(x, y)
print("x =", x, "y =", y)  # Output: x = 10 y = 5