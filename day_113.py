"""
Write a program to handle multiple exceptions.
"""

def handle_multiple_exceptions():
    try:
        # Code that may raise exceptions
        result = 10 / 0
        data = [1, 2, 3]
        print(data[5])
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except IndexError:
        print("Error: Index out of range.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    handle_multiple_exceptions()