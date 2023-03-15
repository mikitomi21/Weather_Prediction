import numpy as np

class Linear_reg:
    def __init__(self):
        #self.theta = [0, 0, 0]
        self.theta = [0, 0]


    def get_theta(self):
        return self.theta


    def fit(self, x_train, y_train):
        x_mat = np.column_stack((np.ones(len(x_train)),x_train))
        x_mat_tra = x_mat.T
        y_mat = np.reshape(y_train,(y_train.shape[0],1))
        self.theta = np.dot(np.dot(np.linalg.inv(np.dot(x_mat_tra, x_mat)), x_mat_tra), y_mat)
    

    def mse(self, x_test, y_test):
        sum = 0
        lenght = len(x_test)
        for i in range(lenght):
            sum += pow(((self.theta[1]*x_test[i]+self.theta[0])-y_test[i]),2)
        return sum/lenght
    
    
    def mae(self, x_test, y_test):
        sum = 0
        lenght = len(x_test)
        for i in range(lenght):
            sum += abs((self.theta[1]*x_test[i]+self.theta[0])-y_test[i])
        return sum/lenght

    def __str__(self) -> str:
        #return f"0 = {self.theta[2]}z + {self.theta[1]}x + {self.theta[0]}y"
        return f"0 = {self.theta[1]}x + {self.theta[0]}y"


class Autoregressive:
    def __init__(self):
        pass


    def fit(self, x_train, y_train):
        p = 10
        linear_model = Linear_reg()
        linear_model.fit(x_train, y_train)
        theta = linear_model.get_theta()
        x_mat = np.column_stack((np.ones(len(x_train)), x_train))
        

        y_pred = []
        for i in range(p, len(x_mat)):
            x_input = x_mat[i-p:i]
            y_hat = np.dot(theta.T,x_input.T)
            y_pred.append(y_hat)
                
        return y_pred
    