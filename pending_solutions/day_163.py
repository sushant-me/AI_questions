"""
Capitalize first letter of each word.
"""

def capitalize_first_letter(text):
    return ' '.join(word.capitalize() for word in text.split())

# Example usage
input_text = "hello world from https://example.com"
output_text = capitalize_first_letter(input_text)
print(output_text)  # Output: "Hello World From https://example.com"