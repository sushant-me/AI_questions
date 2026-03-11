""" Python Programming Questions """

# Task: Write a function to reverse a string without using slicing.

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage:
input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"