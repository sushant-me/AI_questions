"""
Write a program to find the least common multiple (LCM).
"""

def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    return abs(a * b) // gcd(a, b)

# Example usage:
# print(lcm(12, 15))  # Output: 60