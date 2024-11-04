import numpy as np
import time

from StrassensAlgorithm import StrassensAlgorithmMethod


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

    def elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            raise Exception("Timing has not been started or stopped.")
        return self.end_time - self.start_time


if __name__ == "__main__":
    for x in range(0,100):
        matrix_a = np.random.rand(100, 100)
        matrix_b = np.random.rand(100, 100)

        # Initialize and start the Timing class
        timer = Timing()
        timer.start()

        # Call the Strassen's algorithm method
        result = StrassensAlgorithmMethod.Strassens(matrix_a, matrix_b)

        timer.stop()
        # print(f"Time taken for matrix multiplication: {timer.elapsed_time()} seconds")
        print(timer.elapsed_time())
