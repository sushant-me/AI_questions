"""
Use lambda to multiply numbers in a list.
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)