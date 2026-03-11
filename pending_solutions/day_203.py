import numpy as np

def add_matrices(matrix1, matrix2):
    """ Perform matrix addition using NumPy. """
    return np.add(matrix1, matrix2)

# Example usage:
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = add_matrices(matrix1, matrix2)
print(result)