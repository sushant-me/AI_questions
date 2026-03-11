def print_multiplication_table(number):
    """
    Write a program to print the multiplication table of a number.
    """
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Example usage
print_multiplication_table(5)