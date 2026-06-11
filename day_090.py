def count_vowels(s):
    """
    Write a function to count vowels in a string.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)