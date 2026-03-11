"""
Create random name picker.
"""

import random

def pick_random_name(names):
    return random.choice(names)

names_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(pick_random_name(names_list))