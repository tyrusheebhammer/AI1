import numpy as np
class HillClimbing:
    start_x = -1
    end_x = 2

    def f(self, x):
        return -1 * (x - 1) * (x - 1) + 2

    def max(self):
        dx = 0.01


