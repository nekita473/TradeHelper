import numpy as np


class RMA:
    def __init__(self, n):
        self.n = n

    def fit(self, data):
        rma = np.zeros(len(data))
        rma[0] = data[0]
        for i in range(1, len(data)):
            rma[i] = ((self.n-1) * rma[i-1] + data[i])/self.n
        return rma
