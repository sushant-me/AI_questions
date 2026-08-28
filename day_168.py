""" Check perfect number. """

def is_perfect_number(num):
    if num <= 1:
        return False
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.extend([i, num // i])
    return sum(divisors) == num

# Example usage:
number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")