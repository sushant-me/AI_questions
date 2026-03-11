"""
Print number pyramid.
"""

def print_number_pyramid(height):
    for i in range(1, height + 1):
        # Print leading spaces
        for j in range(height - i):
            print(" ", end="")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end="")
        # Print mirrored numbers
        for l in range(i - 1, 0, -1):
            print(l, end="")
        print()

# Example usage
print_number_pyramid(5)