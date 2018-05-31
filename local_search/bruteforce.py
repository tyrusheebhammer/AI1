# Brute force search looks at every possible value within the interval
# to find the maximum or minimum value for a function. Greater
# accuracy is determined by the size of the 'dx'. Guaranteed to find the
# optimal solution, but may be very slow!
import numpy as np


class BruteForce:
    start_x = -1
    end_x = 2

    def f(self, x):
        return -1 * (x - 1) * (x - 1) + 2

    def max(self):
        max_f = self.f(self.start_x)
        max_x = self.start_x
        dx = 0.1

        for i in np.arange(self.start_x, self.end_x + dx, dx):
            current_f = self.f(i)
            if current_f > max_f:
                max_x = i
                max_f = current_f
                print("x: %f  max_f: %f" % (max_x, max_f))

        return max_x, max_f
