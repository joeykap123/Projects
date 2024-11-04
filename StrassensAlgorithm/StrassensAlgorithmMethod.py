import numpy as np

# Strassen's Product Rules
# M1 = (A11 + A22) X (B11 + B22)
# M2 = (A21 + A22) X B11
# M3 = A11 X (B12 - B22)
# M4 = A22 X (B21 - B11)
# M5 = (A11 + A12) X B22
# M6 = (A21 - A11) X (B21 + B12)
# M7 = (A12 - A22) X (B21 + B22)

# C11 = M1 + M4 - M5 + M7
# C12 = M3 + M5
# C21 = M2 + M4
# C22 = M1 - M2 + M3 + M6


def Strassens(matrix_a, matrix_b):
    """
        Strassens() performs a simple version of Strassen's algorithm, solely for 2x2 matrices.
        :np.array arg0: The first matrix to be multiplied, represented by np.array()
        :np.array arg1: The second matrix to be multiplied, represented by np.array()
    """

    # First, ensure that both matrices are of dimensions 2x2 for this specific algorithm
    assert matrix_a.shape == (2, 2) and matrix_b.shape == (2, 2), "Both matrices must be 2x2."

    # Split matrix_A into respective quadrants
    A11, A12, A21, A22 = matrix_a[0, 0], matrix_a[0, 1], matrix_a[1, 0], matrix_a[1, 1]
    # Split matrix_b into respective quadrants
    B11, B12, B21, B22 = matrix_b[0, 0], matrix_b[0, 1], matrix_b[1, 0], matrix_b[1, 1]

    # Find each value, M, which corresponds to Strassen's algorithm
    M1 = (A11 + A22) * (B11 + B22)
    M2 = (A21 + A22) * B11
    M3 = A11 * (B12 - B22)
    M4 = A22 * (B21 - B11)
    M5 = (A11 + A12) * B22
    M6 = (A21 - A11) * (B11 + B12)
    M7 = (A12 - A22) * (B21 + B22)

    # Find each entry of the product matrix, C.
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Put the results of each C entry into a matrix and return this matrix.
    result = np.array([[C11, C12], [C21, C22]])
    return result


if __name__ == "__main__":
    # Initialize two matrices to be multiplied together
    a = np.array([[3, -4], [12, 15]])
    b = np.array([[1, 2], [3, 4]])

    print(Strassens(a, b))
