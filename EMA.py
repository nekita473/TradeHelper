import numpy as np


class EMA:
    def __init__(self, n, mode='EMA'):
        super().__init__()
        if mode == 'MMA':
            self.alpha = 1/n
        else:
            self.alpha = 2 / (n + 1)

    def fit(self, data):
        ema = np.zeros(len(data))
        ema[0] = data[0]
        for i in range(1, len(data)):
            ema[i] = self.alpha * data[i] + (1 - self.alpha) * ema[i - 1]
        return ema
