import numpy as np

class KindOfFall:
    SUNNY = 0
    RAIN = 1
    SNOW = 2

class Weather:
    
    def __init__(self, temp_avg, temp_min=None, temp_max=None, fall=None, k_fall=None):
        self.temp_avg = temp_avg
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.fall = fall
        if k_fall.all() != None:
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
    