def decimal_to_hexadecimal(decimal_number):
    """
    Write a program to convert decimal to hexadecimal.
    """
    return hex(decimal_number).replace("0x", "").upper()

# Example usage:
decimal_number = 255
print(f"The hexadecimal representation of {decimal_number} is {decimal_to_hexadecimal(decimal_number)}")