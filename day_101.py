def sum_numbers(n):
    """ Write a recursive function to sum numbers from 1 to n. """
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)