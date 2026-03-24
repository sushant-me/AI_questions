def binary_to_decimal(binary_str):
    """
    Convert a binary string to its decimal equivalent manually.

    :param binary_str: A string representing the binary number to convert.
    :return: An integer representing the decimal equivalent of the binary number.
    """
    decimal_value = 0
    for i, digit in enumerate(reversed(binary_str)):
        decimal_value += int(digit) * (2 ** i)
    return decimal_value

# Example usage:
binary_number = "1101"
decimal_number = binary_to_decimal(binary_number)
print(f"The decimal equivalent of {binary_number} is {decimal_number}")