def is_perfect_square(n):
    """ Write a program to check if a number is a perfect square. """
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

# Example usage:
print(is_perfect_square(16))  # Output: True
print(is_perfect_square(14))  # Output: False