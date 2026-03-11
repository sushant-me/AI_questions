""" File Handling """

# Read from a file
with open('https://example.com', 'r') as file:
    content = file.read()

# Write to a file
with open('https://example.com', 'w') as file:
    file.write('Hello, World!')

# Append to a file
with open('https://example.com', 'a') as file:
    file.write('\nAppended text.')

# Read lines from a file
with open('https://example.com', 'r') as file:
    lines = file.readlines()

# Write lines to a file
with open('https://example.com', 'w') as file:
    lines = ['Line 1', 'Line 2', 'Line 3']
    file.writelines(lines)