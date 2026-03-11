"""
Use random module to generate numbers.
"""

import random

# Generate a random integer between 1 and 100
random_integer = random.randint(1, 100)
print("Random Integer:", random_integer)

# Generate a random float between 0 and 1
random_float = random.random()
print("Random Float:", random_float)

# Generate a random choice from a list
my_list = [1, 2, 3, 4, 5]
random_choice = random.choice(my_list)
print("Random Choice:", random_choice)