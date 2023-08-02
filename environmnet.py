import numpy as np


class Env:
    def __init__(self, l_bot, l_top, r_bot, r_top) -> None:
        self.l_bot = l_bot
        self.l_top = l_top
        self.r_bot = r_bot
        self.r_top = r_top

    def get_floor_uniform(self) -> np.ndarray:
        l_idx = np.random.randint(low=0, high=self.l_top-self.l_bot)
        r_idx = np.random.randint(low=0, high=self.r_top-self.r_bot)
        l_floor = l_idx - abs(self.l_bot)
        r_floor = r_idx - abs(self.r_bot)
        return (l_idx, r_idx, l_floor, r_floor)
