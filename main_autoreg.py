import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import *
from model import AutoReg

data = get_data()

train_data, test_data = split_data_asc(data)

x_train = train_data["Avg_Temp_Pre_Day"].to_numpy()
y_train = train_data["Avg_Temp"].to_numpy()

x_test = test_data["Avg_Temp_Pre_Day"].to_numpy()
y_test = test_data["Avg_Temp"].to_numpy()

linear = AutoReg(10)
#print(linear.theta)

# Testing normal fiting

'''
y_pred = []
x_test_temp = x_test.copy()
y_test_temp = y_test.copy()

for i in range(366): 
    linear.fit(x_train[-linear.get_lag():], y_train[-linear.get_lag():])
    y_pred.append(linear.get_theta()[0])
    x_train = np.append(x_train, x_test_temp[0])
    y_train = np.append(y_train, y_test_temp[0])
    x_test_temp = np.delete(x_test_temp, 0)
    y_test_temp = np.delete(y_test_temp, 0)

x = np.arange(366)
plt.plot(x, y_test)
plt.plot(x, y_pred, color="red")
plt.show()

'''

# Testing fiting with git

y_pred = []
linear.fit_with_git(x_train, y_train)

x_test_temp = x_test.copy()
y_test_temp = y_test.copy()

for i in range(366): 
    linear.fit_with_git(x_train, y_train)
    y_pred.append(linear.get_theta()[0])
    x_train = np.append(x_train, x_test_temp[0])
    y_train = np.append(y_train, y_test_temp[0])
    x_test_temp = np.delete(x_test_temp, 0)
    y_test_temp = np.delete(y_test_temp, 0)

x = np.arange(366)
plt.plot(x, y_test)
plt.plot(x, y_pred, color="red")
plt.show()