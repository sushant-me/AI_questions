def sum_of_primes(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return sum(num for num in range(start, end + 1) if is_prime(num))

# Example usage
print(sum_of_primes(1, 10))  # Output should be the sum of prime numbers between 1 and 10