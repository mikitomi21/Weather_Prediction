import numpy as np
from data import *
import matplotlib.pyplot as plt

def relu(x):
    return max(0,x)
    
def sigmoid(x):
    return 1/(1+np.exp(-x))
    
def derivative(x):
    return x*(1-x)

class NeuralNetwork:
    number_of_trains = 0
    teach_freq = 2
    n_neurons = 0
    def __init__(self, x, y, n_neurons):
        self.input = x
        self.n_neurons = n_neurons

        self.weight1 = np.random.rand(np.shape(self.input)[1], n_neurons)
        self.weight2 = np.random.rand(n_neurons, n_neurons)
        self.weight3 = np.random.rand(n_neurons, 1)

        self.biases1 = np.zeros((1, n_neurons))
        self.biases2 = np.zeros((1, n_neurons))

        self.y = y
        self.output = np.zeros(np.shape(y)[0])
        
        self.rate_learning = 0.00000001

    
    def masking(self):
        if np.isfinite(self.weight1).all():
            self.weight1 = np.random.rand(np.shape(self.input)[1], self.n_neurons)
        if np.isfinite(self.weight2).all():
            self.weight2 = np.random.rand(self.n_neurons, self.n_neurons)
        if np.isfinite(self.weight3).all():
            self.weight3 = np.random.rand(self.n_neurons, 1)

    def feed_forward(self):
        self.masking()
        self.layer1 = np.dot(self.input, self.weight1) + self.biases1
        self.layer2 = np.dot(self.layer1, self.weight2) + self.biases2
        self.output = np.dot(self.layer2, self.weight3)

        self.number_of_trains += 1

    def propra_back(self):
        output_error = (2*(self.y - self.output) * derivative(self.output))

        layer_error2 = np.dot(output_error, self.weight3.T) * derivative(self.layer2)
        layer_error1 = np.dot(layer_error2, self.weight2.T) * derivative(self.layer1)

        self.weight3 += self.rate_learning * np.dot(self.layer2.T, output_error)
        self.weight2 += self.rate_learning * np.dot(self.layer1.T, layer_error2)
        self.weight1 += self.rate_learning * np.dot(self.input.T,  layer_error1)

        self.biases2 += self.rate_learning * np.sum(layer_error2, axis=0, keepdims=True)
        self.biases1 += self.rate_learning * np.sum(layer_error1, axis=0, keepdims=True)

    def train(self, x_train, y_train):
        self.input = x_train
        self.y = y_train
        self.feed_forward()
        #if self.number_of_trains % self.teach_freq == 0:
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
    


train_data = get_data()

x_train_org = train_data["Avg_Temp_Pre_Day"].to_numpy()
x_train_org = np.reshape(x_train_org, (np.shape(x_train_org)[0], 1))
y_train_org = train_data["Avg_Temp"].to_numpy()
y_train_org = np.reshape(y_train_org, (np.shape(y_train_org)[0], 1))
x_train = standardize(x_train_org, x_train_org)
y_train = standardize(y_train_org, y_train_org)

network = NeuralNetwork(x_train[0:7].T, y_train[7], 1)

y_output = np.zeros(len(x_train)-7)
y_pred = np.zeros(len(x_train)-7)
for i in range(len(x_train)-7):
    network.train(x_train[i:i+7].T, y_train[i+7])
    y_output[i] = y_train[i+7]
    y_pred[i] = network.output[0]
