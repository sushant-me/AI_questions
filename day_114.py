"""
Write a program to create a custom exception.
"""

class CustomException(Exception):
    """Custom exception class for handling specific errors."""
    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message)

# Example usage
try:
    raise CustomException("This is a custom error message.")
except CustomException as e:
    print(e)