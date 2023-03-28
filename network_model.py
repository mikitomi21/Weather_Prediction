import numpy as np
from data import *
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)
    
def sigmoid(x):
    return 1/(1+np.exp(-x))
    
def derivative(x):
    return x*(1-x)

class NeuralNetwork:
    def __init__(self, x, y, n_neurons):
        self.input = x
        self.weight1 = np.random.rand(np.shape(self.input)[1], n_neurons)
        self.weight2 = np.random.rand(n_neurons, 1)
        self.biases = np.zeros((1, n_neurons))
        self.y = y
        self.output = np.zeros((np.shape(y)[0],1))
        self.rate_learning = 0.0001
    
    def feed_forward(self):
        self.layer = relu(np.dot(self.input, self.weight1) + self.biases)
        self.output = relu(np.dot(self.layer, self.weight2))

    def propra_back(self):
        output_error = (2*(self.y - self.output) * derivative(self.output))
        layer_error = np.dot(output_error, self.weight2.T) * derivative(self.layer)

        self.weight2 += self.rate_learning * np.dot(self.layer.T, output_error)
        self.weight1 += self.rate_learning * np.dot(self.input.T,  layer_error)
        self.biases += self.rate_learning * np.sum(layer_error, axis=0, keepdims=True)

    def train(self, x, y):
        self.input = x
        self.y = y
        self.feed_forward()
        self.propra_back()


'''
X = np.array([0.1,0.2,0.3,0.4,0.5,0.5,0.4,0.3,0.2,0.1])
X = np.reshape(X, (np.shape(X)[0], 1))
y = np.array([0.2,0.3,0.4,0.5,0.5,0.4,0.3,0.2,0.1,0])
y = np.reshape(y, (np.shape(y)[0], 1))
'''


data = get_data()

train_data, test_data = split_data(data)
train_data = get_data()
x_train = train_data["Avg_Temp_Pre_Day"].to_numpy()
x_train = np.reshape(x_train, (np.shape(x_train)[0], 1))
y_train = train_data["Avg_Temp"].to_numpy()
y_train = np.reshape(y_train, (np.shape(y_train)[0], 1))

x_train = standardize(x_train, x_train)
y_train = standardize(y_train, y_train)

x_test = test_data["Avg_Temp_Pre_Day"].to_numpy()
y_test = test_data["Avg_Temp"].to_numpy()
network = NeuralNetwork(x_train[0:7].T, y_train[7], 2)

sum1 = 0
sum2 = 0
lenght = len(x_train)-7
y_output = []
y_pred = []
for i in range(lenght):
    network.train(x_train[i:i+7].T, y_train[i+7])
    y_output.append(y_train[i+7])
    y_pred.append(network.output[0])
    #print(f"\ni:{i}")
    #print(f"y:{network.y}")
    #print(f"output:{network.output}")
    sum1 += (network.output - network.y)
    sum2 += pow((network.output - network.y), 2)
print(f"MSE: {sum2/lenght}")
print(f"MAE: {sum1/lenght}")
   
x = np.arange(lenght)
plt.plot(x, y_output, 'b')
plt.plot(x, y_pred, 'r')
plt.xlabel('Avg_Temp_Pre_Day')
plt.ylabel('Avg_Temp')
plt.show()


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