"""
Use NumPy to create array.
"""

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Create an array with zeros
array_zeros = np.zeros((3, 4))

# Create an array with ones
array_ones = np.ones((2, 3))

# Create an array with a specific shape and fill with a constant value
array_full = np.full((2, 2), 7)

# Create an array with a sequence of numbers
array_arange = np.arange(0, 10, 2)

# Create an array with random numbers
array_random = np.random.rand(2, 2)

# Create an identity matrix
array_identity = np.eye(3)

# Create an array with random integers
array_random_int = np.random.randint(1, 10, (3, 3))