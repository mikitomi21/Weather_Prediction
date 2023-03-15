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
    def __init__(self, lag=3):
        self.lag = lag
        self.theta = np.array([0,0])


    def get_lag(self):
        return self.lag

    
    def get_theta(self):
        return self.theta


    def fit(self, x_train, y_train):
        model = Linear_reg()
        model.fit(x_train, y_train)
        self.theta = model.get_theta()
        '''
         X = np.array(x_train[len(x_train)-self.lag:len(x_train)])
        #print(np.shape(X))
        x_mat = np.column_stack((np.ones(len(X)), X))
        print(np.shape(x_mat))
        y = y_train[len(x_train)-self.lag:len(x_train)]
        #print(np.shape(y))
        y_mat = np.reshape(y,(y.shape[0],1))
        print(np.shape(y_mat))
        print(np.matmul(X.T, X))
        self.theta = np.dot(np.dot(np.linalg.inv(np.dot(x_mat.T, x_mat)), x_mat.T), y_mat)
        '''
       
        
    
    def predict(self, x_test):
        # Dodaj kolumnę z jedynkami do danych testowych
        x_test = np.column_stack((np.ones(len(x_test)), x_test))
        
        # Przygotuj macierz danych dla predykcji
        
        # Oblicz predykcję na podstawie wyestymowanych parametrów
        y_pred = x_test.dot(self.theta)
        
        return y_pred
    