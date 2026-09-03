"""
Print inverted pyramid.
"""

height = 5

for i in range(height, 0, -1):
    print(' ' * (height - i) + '*' * (2 * i - 1))