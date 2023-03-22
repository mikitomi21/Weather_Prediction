import numpy as np

def relu(x):
        return max(0, x)
    
def sigmoid(x):
    return 1/(1+np.exp(-x))
    
def sigmoid_derivative(x):
    return x*(1-x)

class NeuralNetwork:
    def __init__(self, x, y, n_neurons):
        self.input = x
        self.weight1 = np.random.rand(np.shape(self.input)[1], n_neurons)
        self.weight2 = np.random.rand(n_neurons, 1)
        self.y = y
        self.output = np.zeros(np.shape(y)[0])
    
    def feed_forward(self):
        self.layer = sigmoid(np.dot(self.input, self.weight1))
        self.output = sigmoid(np.dot(self.layer, self.weight2))

    def propra_back(self):
        self.weight2 += np.dot(self.layer.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        self.weight1 += np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weight2.T) * sigmoid_derivative(self.layer)))

    def train(self):
         self.feed_forward()
         self.propra_back()



X = np.array([1,2,3,4,5,5,4,3,2,1])
X = np.reshape(X, (np.shape(X)[0], 1))
y = np.array([2,3,4,5,5,4,3,2,1,0])
y = np.reshape(y, (np.shape(y)[0], 1))
network = NeuralNetwork(X, y, 5)

'''
print(network.input)
print(network.weight1)
print(network.weight2)
print(network.y)
print(network.output)
'''


'''
network.feed_forward()
print("Wynik po nauczaniu")
print(network.output)

print("Wagi po powrocie")
network.propra_back()

print(network.weight1)
print(network.weight2)
'''

for i in range(100):
     print(np.reshape(network.output, (1, np.shape(network.output)[0])))
     network.train()
