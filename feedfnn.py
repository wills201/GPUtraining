import numpy as np
class FFNN:
    def __init__(self):
        self.input = x
        self.weight = None
        self.b = None
        self.output = y
        
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def forward(self,x):
        return np.dot(x, self.weight.T) + self.b


    