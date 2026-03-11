"""
Python Questions (151–200)
"""

# 151. Write a function that takes a list of integers and returns a new list with all duplicates removed.
def remove_duplicates(nums):
    return list(set(nums))

# 152. Create a decorator that logs the arguments with which a function is called.
import functools
def log_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# 153. Write a function that checks if a given number is a prime number.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 154. Implement a simple caching mechanism using a dictionary.
class SimpleCache:
    def __init__(self):
        self.cache = {}
    
    def get(self, key):
        return self.cache.get(key, None)
    
    def set(self, key, value):
        self.cache[key] = value
    
    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

# 155. Write a function that finds the nth Fibonacci number using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 156. Create a generator that yields the squares of numbers from 1 to n.
def square_numbers(n):
    for i in range(1, n+1):
        yield i**2

# 157. Write a function that checks if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

# 158. Implement a simple HTTP GET request using the requests library.
import requests
def get_request(url):
    response = requests.get(url)
    return response.text

# 159. Create a class that implements the iterator protocol.
class MyIterator:
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

# 160. Write a function that calculates the factorial of a number using an iterative approach.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# ... (Continue with other questions in a similar format)