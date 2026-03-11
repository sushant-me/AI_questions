"""
Write a program to shuffle a list randomly.
"""

import random

def shuffle_list(input_list):
    random.shuffle(input_list)
    return input_list

# Example usage:
my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print(shuffled_list)