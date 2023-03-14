import numpy as np

class Linear_reg:
    def __init__(self):
        self.theta = [0, 0, 0]

    def fit(self, x_train, y_train, z_train):
        x_mat = np.column_stack((np.ones(len(x_train)),x_train, z_train))
        x_mat_tra = x_mat.T
        y_mat = np.reshape(y_train,(y_train.shape[0],1))
        self.theta = np.dot(np.dot(np.linalg.inv(np.dot(x_mat_tra, x_mat)), x_mat_tra), y_mat)
    
    def mse(self, x_test, y_test, z_test):
        sum = 0
        lenght = len(x_test)
        for i in range(lenght):
            sum += pow(((self.theta[2]*z_test[i]+self.theta[1]*x_test[i]+self.theta[0])-y_test[i]),2)
        return sum/lenght