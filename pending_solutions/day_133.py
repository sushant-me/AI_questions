def square_generator():
    """ Write a generator to yield squares of numbers. """
    num = 1
    while True:
        yield num ** 2
        num += 1