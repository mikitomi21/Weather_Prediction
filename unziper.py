# 1.  Download data from https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/klimat/
# 2.  DOWNLOAD_FOLDER - type your download path
# 3.  PROJECT_DATA_FOLDER - type your path to 'data' folder in the project
# 4.  YEAR_START & YEAR_END - type years range that you have downloaded

import zipfile 
import os
import shutil
DOWNLOAD_FOLDER = "C:\\Users\\maste\\Downloads\\"
PROJECT_DATA_FOLDER = "E:\\XXX\Studia\\SEMESTR IV\\Sztuczna inteligencja\\Weather_Prediction\\data\\"
YEAR_START = 1951
YEAR_END = 2023
for year in range (YEAR_START, YEAR_END):
    if year > 2000:
        for i in range(1, 13):

            if i < 10:
                path = DOWNLOAD_FOLDER + str(year) + "_0" + str(i) + "_k.zip"
                fileToDelete = DOWNLOAD_FOLDER +"k_d_t_0"+ str(i) + "_"+ str(year) + ".csv"
            else:
                path = DOWNLOAD_FOLDER + str(year) + "_" + str(i) + "_k.zip"
                fileToDelete = DOWNLOAD_FOLDER + "k_d_t_"+ str(i) + "_"+ str(year) + ".csv"
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(DOWNLOAD_FOLDER)
            os.remove(fileToDelete)
            os.remove(path)
    
        for i in range(1, 13):
            newPath = PROJECT_DATA_FOLDER + str(year) 
            if not os.path.exists(newPath):
                os.makedirs(newPath)
            if i < 10:
                file = "k_d_0" + str(i) + "_" + str(year) + ".csv"
            else:
                file = "k_d_" + str(i) + "_" + str(year) + ".csv"
            
            oldPath = DOWNLOAD_FOLDER + file
        
            shutil.move(oldPath, newPath)
    else:
        path = DOWNLOAD_FOLDER + str(year) +  "_k.zip"
        fileToDelete = DOWNLOAD_FOLDER +"k_d_t_" + str(year) + ".csv"
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(DOWNLOAD_FOLDER)
        os.remove(fileToDelete)
        os.remove(path)

        newPath = PROJECT_DATA_FOLDER + str(year) 
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        file = "k_d_"+ str(year) + ".csv"    
        oldPath = DOWNLOAD_FOLDER + file
        shutil.move(oldPath, newPath)