def gcd(a, b):
    """ Write a program to find the greatest common divisor (GCD). """
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(gcd(48, 18))  # Output: 6