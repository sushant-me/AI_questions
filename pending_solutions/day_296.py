def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    
    # Determine the sign of the result
    negative = (dividend < 0) != (divisor < 0)
    
    # Work with absolute values to simplify the division process
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    temp = 0
    
    # Iterate over possible bit positions
    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient |= 1 << i
    
    return -quotient if negative else quotient

# Example usage:
result = divide(-20, 5)
print(result)  # Output: -4