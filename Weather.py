import numpy as np

class KindOfFall:
    SUNNY = 1
    RAIN = 2
    SNOW = 3

class Weather:
    def __init__(self, temp):
        self.temp = temp
    
    def __init__(self, temp, fall):
        self.temp = temp
        self.fall = fall

    def __init__(self, temp, fall, k_fall):
        self.temp = temp
        self.fall = fall
        self.k_fall = self.get_k_fall(k_fall)
    
    def get_k_fall(self,k_fall):
        k_fall_temp = np.zeros(len(k_fall))
        for i in range(len(k_fall)):
            if k_fall[i] == "W":
                k_fall_temp[i] = KindOfFall.RAIN
            elif k_fall[i] == "S":
                k_fall_temp[i] = KindOfFall.SNOW
            else:
                k_fall_temp[i] = KindOfFall.SUNNY
        return k_fall_temp
    
