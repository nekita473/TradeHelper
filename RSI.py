from EMA import EMA
import numpy as np


class RSI:
    def __init__(self, n):
        super().__init__()
        self.n = n

    def fit(self, data):
        u = np.zeros(len(data))
        d = np.zeros(len(data))
        for i in range(1, len(data)):
            if data[i] > data[i-1]:
                u[i] = data[i] - data[i-1]
            else:
                d[i] = data[i-1] - data[i]
        ema_u = EMA(self.n, 'MMA').fit(u)
        ema_d = EMA(self.n, 'MMA').fit(d)
        rs = ema_u/ema_d
        rsi = 100 - 100/(1+rs)
        return rsi
