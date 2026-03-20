def fibonacci_series(n):
    """
    Write a program to print Fibonacci series up to n terms.
    """
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("0")
    else:
        a, b = 0, 1
        print("Fibonacci series up to", n, "terms:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b

# Example usage:
fibonacci_series(10)