""" Write a program to validate user input using exceptions. """

def get_valid_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            # Example validation: check if input is a number
            if user_input.isdigit():
                return int(user_input)
            else:
                raise ValueError("Invalid input. Please enter a number.")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    valid_number = get_valid_input("Please enter a number: ")
    print(f"You entered: {valid_number}")

if __name__ == "__main__":
    main()