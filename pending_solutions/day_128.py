""" Iterators & Generators """


class SimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

def simple_generator(data):
    for item in data:
        yield item

# Example usage of the iterator
simple_iter = SimpleIterator([1, 2, 3, 4, 5])
for value in simple_iter:
    print(value)

# Example usage of the generator
for value in simple_generator([1, 2, 3, 4, 5]):
    print(value)