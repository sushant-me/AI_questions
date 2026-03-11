"""
11–20: Loops
"""

for i in range(10):
    print(i)

while True:
    user_input = input("Enter 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break