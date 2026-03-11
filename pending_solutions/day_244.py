"""
Implement linear regression.
"""

import numpy as np

def linear_regression(X, y):
    """
    Fit a linear regression model to the data.

    Parameters:
    X (numpy.ndarray): The input features, shape (n_samples, n_features).
    y (numpy.ndarray): The target values, shape (n_samples,).

    Returns:
    numpy.ndarray: The coefficients of the linear model, shape (n_features,).
    """
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    return theta_best

# Example usage:
# X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = np.dot(X, np.array([1, 2])) + 3
# theta = linear_regression(X, y)
# print(theta)