import numpy as np

class NeuralNetwork:
    def __init__(self, x, y, n_neurons):
        self.input = x
        self.weight1 = np.random.rand(np.shape(self.input)[1], n_neurons)
        self.weight2 = np.random.rand(n_neurons, 1)
        self.y = y
        self.output = np.zeros(np.shape(y)[0])