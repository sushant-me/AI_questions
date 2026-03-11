""" Write a program to convert Celsius to Fahrenheit. """

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# Example usage:
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")