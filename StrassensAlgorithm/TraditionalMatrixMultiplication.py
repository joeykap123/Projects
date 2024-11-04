import numpy as np


def MatrixMultiplicationMethod(matrix_a, matrix_b):
    """
        MatrixMultiplicationMethod() represents a naive, matrix multiplication method for matrices of any dimension
        :np.array arg0: The first matrix to be multiplied, represented by np.array()
        :np.array arg1: The second matrix to be multiplied, represented by np.array()
    """
    # Ensure dimensions are compatible for matrix multiplication
    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise Exception("Number of columns in matrix_a must equal the number of rows in matrix_b.")

    # Initialize result matrix C
    matrix_c = np.zeros((matrix_a.shape[0], matrix_b.shape[1]))

    # Perform matrix multiplication
    for i in range(matrix_a.shape[0]):
        for j in range(matrix_b.shape[1]):
            for k in range(matrix_a.shape[1]):
                matrix_c[i, j] += matrix_a[i, k] * matrix_b[k, j]

    return matrix_c


if __name__ == "__main__":
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[3, 4], [5, 6]])
    print(MatrixMultiplicationMethod(a, b))
