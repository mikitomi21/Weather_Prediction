import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import *
from model import Linear_reg

data = get_data()

train_data, test_data = split_data(data)

x_train = train_data["Avg_Temp_Pre_Day"].to_numpy()
y_train = train_data["Avg_Temp"].to_numpy()

x_test = test_data["Avg_Temp_Pre_Day"].to_numpy()
y_test = test_data["Avg_Temp"].to_numpy()

linear = Linear_reg()
linear.fit(x_train, y_train)
print(linear)
print(linear.mse(x_test, y_test))
print(linear.mae(x_test, y_test))

x = np.linspace(min(x_test), max(x_test), 100)
y = float(linear.get_theta()[0]) + float(linear.get_theta()[1]) * x
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Avg_Temp_Pre_Day')
plt.ylabel('Avg_Temp')
plt.show()
