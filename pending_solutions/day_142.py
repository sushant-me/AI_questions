from datetime import datetime

def calculate_date_difference(date1, date2):
    """
    Calculate difference between two dates.

    Args:
    date1 (str): The first date in 'YYYY-MM-DD' format.
    date2 (str): The second date in 'YYYY-MM-DD' format.

    Returns:
    int: The difference in days between the two dates.
    """
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = abs((b - a).days)
    return delta

# Example usage
date1 = '2023-01-01'
date2 = '2023-01-15'
print(calculate_date_difference(date1, date2))  # Output: 14