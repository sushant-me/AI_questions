"""
Write a program to append text to a file.
"""

# Open the file in append mode ('a') or create it if it doesn't exist ('a+')
with open('example.txt', 'a') as file:
    # Append text to the file
    file.write("This is a new line of text.\n")