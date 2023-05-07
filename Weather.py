import numpy as np
from data import standardize
import copy

class KindOfFall:
    SUNNY = 0
    RAIN = 1
    SNOW = 2

class Weather:
    
    def __init__(self, temp_avg, temp_min=None, temp_max=None, fall=None, k_fall=None, cloudiness=None, wind_speed = None, humidity = None, pressure = None):
        self.temp_avg = temp_avg
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.fall = fall
        self.cloudiness = cloudiness
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.pressure = pressure
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
    
    def standardize(self):
        self.temp_avg = standardize(self.temp_avg ,self.temp_avg)
        self.temp_min = standardize(self.temp_avg ,self.temp_avg)
        self.temp_max = standardize(self.temp_avg ,self.temp_avg)

        self.cloudiness = standardize(self.cloudiness ,self.cloudiness)
        self.wind_speed = standardize(self.wind_speed ,self.wind_speed)
        self.humidity = standardize(self.humidity ,self.humidity)
        self.pressure = standardize(self.pressure ,self.pressure)
    
    def join_weather(self):
        weather = copy.copy(self)
        return np.concatenate((
            weather.temp_avg.reshape(-1, 1),
            weather.temp_min.reshape(-1, 1),
            weather.temp_max.reshape(-1, 1),
            weather.fall.reshape(-1, 1),
            weather.k_fall.reshape(-1, 1),
            weather.cloudiness.reshape(-1, 1),
            weather.wind_speed.reshape(-1, 1),
            weather.humidity.reshape(-1, 1),
            weather.pressure.reshape(-1, 1),
        ), axis=1)

    @classmethod
    def to_weather(cls, town):
        return Weather(
            town["Avg_Temp"].to_numpy(),
            town["Min_Temp"].to_numpy(),
            town["Max_Temp"].to_numpy(),
            town["Sum_Fall"].to_numpy(),
            town["Kind_of_Fall"].to_numpy(),
            town["Avg_Cloudiness"].to_numpy(),
            town["Avg_Wind_Speed"].to_numpy(),
            town["Avg_Humidity"].to_numpy(),
            town["Avg_Atmo_Pressure"].to_numpy(),
        )
    