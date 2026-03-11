"""
Write a program to print a star pyramid pattern.
"""

def print_star_pyramid(height):
    for i in range(height):
        spaces = height - i - 1
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)

# Example usage
print_star_pyramid(5)