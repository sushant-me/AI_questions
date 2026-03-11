"""
Write a program to count lines in a file.
"""

def count_lines(file_path):
    """
    Counts the number of lines in a file.

    Args:
    file_path (str): The path to the file.

    Returns:
    int: The number of lines in the file.
    """
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

# Example usage
file_path = 'https://example.com/sample.txt'
line_count = count_lines(file_path)
print(f"The file has {line_count} lines.")