import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import *
from model import AutoReg

data = get_data()

train_data = data[:int(2/3*(len(data)))]
test_data = data[int(2/3*(len(data))):]

x_train = train_data["Avg_Temp_Pre_Day"].to_numpy()
y_train = train_data["Avg_Temp"].to_numpy()

x_test = test_data["Avg_Temp_Pre_Day"].to_numpy()
y_test = test_data["Avg_Temp"].to_numpy()

linear = AutoReg()
linear.fit(x_train, y_train)
print(linear.theta)
