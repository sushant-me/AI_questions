"""
Write a generator to generate even numbers.
"""

def even_number_generator():
    num = 0
    while True:
        yield num
        num += 2

# Example usage:
# even_gen = even_number_generator()
# print(next(even_gen))  # Output: 0
# print(next(even_gen))  # Output: 2
# print(next(even_gen))  # Output: 4