def is_armstrong_number(num):
    # Convert number to string to easily iterate over digits
    digits = str(num)
    # Calculate number of digits
    n = len(digits)
    # Calculate sum of digits each raised to the power of n
    sum_of_powers = sum(int(digit) ** n for digit in digits)
    # Check if sum of powers is equal to the original number
    return sum_of_powers == num

# Example usage
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")