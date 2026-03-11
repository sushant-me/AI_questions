"""
Find LCM of two numbers.
"""

def lcm(a, b):
    """
    Calculate the least common multiple of two numbers.
    
    Args:
    a (int): First number.
    b (int): Second number.
    
    Returns:
    int: The LCM of the two numbers.
    """
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // gcd(a, b)

def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers.
    
    Args:
    a (int): First number.
    b (int): Second number.
    
    Returns:
    int: The GCD of the two numbers.
    """
    while b:
        a, b = b, a % b
    return a

# Example usage:
# result = lcm(12, 15)
# print(result)  # Output: 60