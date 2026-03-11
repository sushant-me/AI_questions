"""
Remove duplicate characters from string.
"""

def remove_duplicates(s):
    return "".join(dict.fromkeys(s))

# Example usage
input_string = "hello world"
output_string = remove_duplicates(input_string)
print(output_string)  # Output: "helo wrd"