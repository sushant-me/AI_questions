"""
Calculate mean using NumPy.
"""

import numpy as np

def calculate_mean(data):
    return np.mean(data)

# Example usage:
data = [1, 2, 3, 4, 5]
mean_value = calculate_mean(data)
print("Mean:", mean_value)