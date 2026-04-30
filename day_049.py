def calculate_average(numbers):
    """
    Write a function to calculate the average of numbers in a list.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)