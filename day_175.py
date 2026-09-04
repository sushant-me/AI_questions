"""
Print Floyd’s triangle.
"""

def print_floyd_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

# Example usage
print_floyd_triangle(5)