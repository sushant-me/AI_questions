def find_two_non_repeating_numbers(arr):
    """
    Write a program to find two non-repeating numbers.
    """
    xor = 0
    for num in arr:
        xor ^= num
    
    # Find a set bit (rightmost) in the xor which is different from its adjacent bits
    right_set_bit = xor & -xor
    
    # Divide the array into two sets and find the XOR of each set
    num1, num2 = 0, 0
    for num in arr:
        if num & right_set_bit:
            num1 ^= num
        else:
            num2 ^= num
    
    return num1, num2

# Example usage
arr = [4, 3, 6, 5, 3, 4]
print(find_two_non_repeating_numbers(arr))  # Output: (5, 6)