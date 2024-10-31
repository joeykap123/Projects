import numpy as np


def MatrixMultiplicationMethod(matrix_a, matrix_b):
    # Check if inputs are of type np.matrix or np.ndarray
    if not isinstance(matrix_a, (np.matrix, np.ndarray)) or not isinstance(matrix_b, (np.matrix, np.ndarray)):
        raise Exception("Both inputs must be NumPy matrices or arrays.")

    # Ensure dimensions are compatible for matrix multiplication
    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise Exception("Number of columns in matrix_a must equal the number of rows in matrix_b.")

    # Initialize the result matrix with zeros
    matrix_c = np.zeros((matrix_a.shape[0], matrix_b.shape[1]))

    # Perform matrix multiplication
    for i in range(matrix_a.shape[0]):
        for j in range(matrix_b.shape[1]):
            for k in range(matrix_a.shape[1]):
                matrix_c[i, j] += matrix_a[i, k] * matrix_b[k, j]

    return matrix_c


if __name__ == "__main__":
    MatrixMultiplicationMethod()
