def check_overflow(a, b):
    """ Write a program to check overflow in addition. """
    try:
        result = a + b
        if (a > 0 and b > 0 and result <= 0) or (a < 0 and b < 0 and result >= 0):
            return True
        else:
            return False
    except OverflowError:
        return True

# Example usage
print(check_overflow(2147483647, 1))  # Output: True
print(check_overflow(-2147483648, -1))  # Output: True
print(check_overflow(10, 5))  # Output: False