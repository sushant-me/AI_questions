import math

def calculate_standard_deviation(data):
    """ Calculate standard deviation. """
    if len(data) == 0:
        return 0.0
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# Example usage:
data = [2, 4, 4, 4, 5, 5, 7, 9]
std_dev = calculate_standard_deviation(data)
print(f"Standard Deviation: {std_dev}")