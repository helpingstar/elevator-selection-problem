import numpy as np


class Env:
    def __init__(self, high=16, low=4) -> None:
        assert high > 0 and low > 0
        self.high = high
        self.low = low
        self.n_floor = high + low - 1

    def get_floor_uniform(self) -> np.ndarray:
        floors = np.random.randint(low=1, high=self.n_floor, size=(2,))
        for i in range(2):
            if floors[i] <= self.low:
                floors[i] = -floors[i]
            else:
                floors[i] = floors[i] - self.low + 1
        return floors
