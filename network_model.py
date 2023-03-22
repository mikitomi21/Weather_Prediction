import numpy as np

class NeuralNetwork:
    def __init__(self, x, y, n_neurons):
        self.input = x
        self.weight1 = np.random.rand(np.shape(self.input)[1], n_neurons)
        self.weight2 = np.random.rand(n_neurons, 1)
        self.y = y
        self.output = np.zeros(np.shape(y)[0])
    
    def feed_forward(self):
        self.label = np.maximum(0, np.dot(self.input, self.weight1))
        self.output = np.maximum(0, np.dot(self.label, self.weight2))

X = np.array([1,2,3,4,5,6])
X = np.reshape(X, (np.shape(X)[0], 1))
y = np.array([2,3,4,5,6,5])
network = NeuralNetwork(X, y, 5)

print(network.input)
print(network.weight1)
print(network.weight2)
print(network.y)
print(network.output)

network.feed_forward()

print(network.output)