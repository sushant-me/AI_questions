def factorial(n):
    """ Write a recursive function for factorial. """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)