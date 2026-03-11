"""
Check if two strings are rotations.
"""

def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    return s1 in (s2 + s2)

# Example usage:
# result = are_rotations("hello", "lohel")
# print(result)  # Output: True