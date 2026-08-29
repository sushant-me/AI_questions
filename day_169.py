"""
Generate prime numbers up to n.
"""

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

# Example usage:
n = 30
print(generate_primes(n))