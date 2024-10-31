import numpy as np
import time
from StrassensAlgorithm import TraditionalMatrixMultiplication


class Timing:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise Exception("Timing has not been started.")
        self.end_time = time.time()

    """
    
    """

    def elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            raise Exception("Timing has not been started or stopped.")
        return self.end_time - self.start_time


if __name__ == "__main__":
    # Within a range of 0 to 100, time the efficiency of traditional matrix multiplication
    for x in range(100, 1_000, 100):
        matrix_a = np.random.rand(x, x)
        matrix_b = np.random.rand(x, x)

        # Initialize and start the Timing class
        timer = Timing()
        timer.start()

        # Run the matrix multiplication
        result = TraditionalMatrixMultiplication.MatrixMultiplicationMethod(matrix_a, matrix_b)

        timer.stop()
        # print(f"Time taken for matrix multiplication: {timer.elapsed_time()} seconds")
        print(timer.elapsed_time())
