import numpy as np

class Linear_reg:
    def __init__(self):
        #self.theta = [0, 0, 0]
        self.theta = np.array([0,0])


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


class AutoReg:
    def __init__(self, lag=8):
        self.lag = lag
        self.theta = np.array([0,0])

    def fit(self, x_train, y_train):
        x_train = np.column_stack((np.ones(len(x_train)), x_train))
        
        X = []
        for i in range(self.lag, len(x_train)):
            X.append(x_train[i-self.lag:i])
        X = np.array(X)
        
        y = y_train[self.lag:]

        #TODO problem z mnożeniem macierzy

        X_tra = np.transpose(X, axes=(0, 2, 1))
        
        print(np.shape(np.matmul(X_tra, X)))
        self.theta = np.dot(np.dot(np.linalg.inv(np.dot(X_tra, X)), X_tra), y)
        
    
    def predict(self, x_test):
        # Dodaj kolumnę z jedynkami do danych testowych
        x_test = np.column_stack((np.ones(len(x_test)), x_test))
        
        # Przygotuj macierz danych dla predykcji
        X_test = []
        for i in range(self.lag, len(x_test)):
            X_test.append(x_test[i-self.lag:i])
        X_test = np.array(X_test)
        
        # Oblicz predykcję na podstawie wyestymowanych parametrów
        y_pred = X_test.dot(self.theta)
        
        return y_pred
    