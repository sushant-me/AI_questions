"""
Create simple calculator using Python.
"""
def calculator():
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide) or 'exit' to quit: ")
        if operation == 'exit':
            break
        if operation in ('add', 'subtract', 'multiply', 'divide'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if operation == 'add':
                print(f"Result: {num1 + num2}")
            elif operation == 'subtract':
                print(f"Result: {num1 - num2}")
            elif operation == 'multiply':
                print(f"Result: {num1 * num2}")
            elif operation == 'divide':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero")
        else:
            print("Invalid operation")

calculator()