def is_power_of_two(n):
    """ Write a program to check if a number is a power of 2. """
    return n > 0 and (n & (n - 1)) == 0

# Example usage:
number = 16
if is_power_of_two(number):
    print(f"{number} is a power of 2.")
else:
    print(f"{number} is not a power of 2.")