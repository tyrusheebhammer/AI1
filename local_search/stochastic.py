# stochastic search chooses a random index in a position array and tests to see if that
# f(x) is the max. The advantage is you can choose the number of times you pull from an
# array, disadvantage is it non-deterministic as it isn't guaranteed to find the global
# maximum

import numpy as np
from random import randint


class Stochastic:
    start_x = -1
    end_x = 2

    def f(self, x):
        return -1 * (x - 1) * (x - 1) + 2

    def max(self):
        dx = 0.01
        x_list = list(np.arange(self.start_x, self.end_x, dx))
        max_f = self.f(self.start_x)
        max_x = self.start_x

        for _ in range(20):
            rand_i = randint(0,len(x_list) - 1)
            current_f = self.f(x_list[rand_i])

            if current_f > max_f:
                max_x = x_list[rand_i]
                max_f = current_f
                print("x: %f  max_f: %f" % (max_x, max_f))

        return max_x, max_f
