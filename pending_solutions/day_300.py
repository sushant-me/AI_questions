"""
Write a program to find all substrings of a string.
"""

def findAllSubstrings(s):
    n = len(s)
    return [s[i: j] for i in range(n) for j in range(i + 1, n + 1)]

# Example usage:
print(findAllSubstrings("abc"))


This function generates all possible substrings of the input string `s` by iterating through all possible starting and ending indices.