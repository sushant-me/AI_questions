def matrix_multiplication(A, B):
    """
    Perform matrix multiplication.

    Args:
    A (list of lists of int): First matrix.
    B (list of lists of int): Second matrix.

    Returns:
    list of lists of int: Resulting matrix after multiplication.
    """
    # Check if the number of columns in A is equal to the number of rows in B
    if len(A[0]) != len(B):
        raise ValueError("The number of columns in A must be equal to the number of rows in B")

    # Initialize the resulting matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result