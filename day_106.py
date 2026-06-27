""" Write a program to read a file line by line. """

# Open the file in read mode
with open('example.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Process each line (e.g., print it)
        print(line.strip())  # Using strip() to remove any leading/trailing whitespace