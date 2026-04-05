
# Example task: Reverse a string
def reverse_string(s):
    return s[::-1]

# Example task: Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example task: Convert a string to a URL slug
def to_slug(s):
    return s.replace(' ', '-').lower()

# Example task: Count occurrences of a substring in a string
def count_substring(s, sub):
    return s.count(sub)

# Example task: Replace a substring in a string
def replace_substring(s, old, new):
    return s.replace(old, new)

# Example task: Remove all non-alphanumeric characters from a string
def remove_non_alphanumeric(s):
    return ''.join(c for c in s if c.isalnum())

# Example task: Convert a string to title case
def to_title_case(s):
    return s.title()

# Example task: Capitalize the first letter of a string
def capitalize_first_letter(s):
    return s.capitalize()

# Example task: Convert a string to lowercase
def to_lowercase(s):
    return s.lower()

# Example task: Convert a string to uppercase
def to_uppercase(s):
    return s.upper()

# Example task: Split a string into a list of words
def split_string(s):
    return s.split()

# Example task: Join a list of strings into a single string
def join_strings(lst):
    return ''.join(lst)

# Example task: Get the length of a string
def get_length(s):
    return len(s)

# Example task: Check if a string is empty
def is_empty(s):
    return len(s) == 0

# Example task: Get the first character of a string
def get_first_char(s):
    return s[0]

# Example task: Get the last character of a string
def get_last_char(s):
    return s[-1]

# Example task: Get a substring from a string
def get_substring(s, start, end):
    return s[start:end]

# Example task: Concatenate two strings
def concatenate_strings(s1, s2):
    return s1 + s2

# Example task: Check if a string contains a substring
def contains_substring(s, sub):
    return sub in s

# Example task: Remove leading and trailing whitespace from a string
def strip_whitespace(s):
    return s.strip()

# Example task: Remove leading whitespace from a string
def lstrip_whitespace(s):
    return s.lstrip()

# Example task: Remove trailing whitespace from a string
def rstrip_whitespace(s):
    return s.rstrip()