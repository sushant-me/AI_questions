def factorial(n):
    """
    Write a function to find the factorial of a number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)