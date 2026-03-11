"""
Strings Advanced
"""

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    return sum(1 for char in s if char in "aeiouAEIOU")

def replace_substring(s, old, new):
    return s.replace(old, new)

def split_string(s, delimiter):
    return s.split(delimiter)

def join_strings(lst, delimiter):
    return delimiter.join(lst)

def main():
    text = "Hello, World!"
    print(reverse_string(text))  # Output: !dlroW ,olleH
    print(is_palindrome(text))  # Output: False
    print(count_vowels(text))  # Output: 3
    print(replace_substring(text, "World", "Python"))  # Output: Hello, Python!
    print(split_string(text, ", "))  # Output: ['Hello', 'World!']
    print(join_strings(['Hello', 'World!'], ", "))  # Output: Hello, World!

if __name__ == "__main__":
    main()