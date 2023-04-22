import numpy as np
from data import *
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0,x)
    
def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative(x):
    return 1 - np.tanh(x)**2

class NeuralNetwork:
    def __init__(self, x, y, n_neurons):
        self.input = x
        self.weight1 = np.random.rand(np.shape(self.input)[1], n_neurons)
        self.weight2 = np.random.rand(n_neurons, 1)
        self.biases = np.zeros((1, n_neurons))
        self.y = y
        self.output = np.zeros(np.shape(y)[0])
        self.rate_learning = 0.1
    
    def feed_forward(self):
        self.layer = sigmoid(np.dot(self.input, self.weight1) + self.biases)
        self.output = np.dot(self.layer, self.weight2)

    def propra_back(self):
        output_error = (2*(self.y - self.output) * derivative(self.output))
        layer_error = np.dot(output_error, self.weight2.T) * derivative(self.layer)

        self.weight2 += self.rate_learning * np.dot(self.layer.T, output_error)
        self.weight1 += self.rate_learning * np.dot(self.input.T,  layer_error)
        self.biases += self.rate_learning * np.sum(layer_error, axis=0, keepdims=True)

    def train(self, x_train, y_train):
        self.input = x_train
        self.y = y_train
        self.feed_forward()
        self.propra_back()
    
    def predict(self, x_test):
        # assert 
        self.input = x_test
        self.feed_forward()
    
    def mse(self, y_output, y_pred):
        mse = 0
        for i in range(len(y_output)):
            mse += pow((y_output[i] - y_pred[i]),2)
        return mse/len(y_output)
    
    def mae(self, y_output, y_pred):
        mae = 0
        for i in range(len(y_output)):
            mae += abs(y_output[i] - y_pred[i])
        return mae/len(y_output)