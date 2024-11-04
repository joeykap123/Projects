import numpy as np


def StrassensRecursive(matrix_a, matrix_b):
    """
        StrassensRecursive() performs a recursive version of Strassen's algorithm, able to compute the product of any two matrices of any dimension
        :np.array arg0: The first matrix to be multiplied, represented by np.array()
        :np.array arg1: The second matrix to be multiplied, represented by np.array()
    """

    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise Exception("Number of columns in matrix_a must equal the number of rows in matrix_b.")

    # BASE CASE WHEN MATRIX IS 1X1
    if matrix_a.shape[0] == 1:
        return matrix_a * matrix_b

    # Ensure the matrix is square and of size 2^n x 2^n by padding with zeros if needed
    n = max(matrix_a.shape[0], matrix_a.shape[1], matrix_b.shape[0], matrix_b.shape[1])
    m = 1 << (n - 1).bit_length()  # Smallest power of 2 greater than or equal to n

    # Pad matrices with 0's if necessary
    a = np.pad(matrix_a, ((0, m - matrix_a.shape[0]), (0, m - matrix_a.shape[1])), mode='constant')
    b = np.pad(matrix_b, ((0, m - matrix_b.shape[0]), (0, m - matrix_b.shape[1])), mode='constant')

    # Split the matrices into 4 different quadrants
    mid = m // 2
    A11, A12, A21, A22 = a[:mid, :mid], a[:mid, mid:], a[mid:, :mid], a[mid:, mid:]
    B11, B12, B21, B22 = b[:mid, :mid], b[:mid, mid:], b[mid:, :mid], b[mid:, mid:]

    # Find M values via the 7 Strassen equations
    M1 = StrassensRecursive(A11 + A22, B11 + B22)
    M2 = StrassensRecursive(A21 + A22, B11)
    M3 = StrassensRecursive(A11, B12 - B22)
    M4 = StrassensRecursive(A22, B21 - B11)
    M5 = StrassensRecursive(A11 + A12, B22)
    M6 = StrassensRecursive(A21 - A11, B11 + B12)
    M7 = StrassensRecursive(A12 - A22, B21 + B22)

    # Use Strassen's algorithm equations to construct matrix C
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Create two matrices of top and bottom
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    # Combine top and bottom matrices to get matrix C
    result = np.vstack((top, bottom))

    # Remove any padding if it was added
    return result[:matrix_a.shape[0], :matrix_b.shape[1]]


if __name__ == "__main__":
    matrix1 = np.array([[3, 2], [2, 4], [9, 0]])
    matrix2 = np.array([[1, 2, 4], [3, 4, 7]])

    print(StrassensRecursive(matrix1, matrix2))
