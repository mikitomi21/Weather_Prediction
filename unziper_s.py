# 1.  Download data from https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/klimat/
# 2.  DOWNLOAD_FOLDER - type your download path
# 3.  PROJECT_DATA_FOLDER - type your path to 'data' folder in the project
# 4.  YEAR_START & YEAR_END - type years range that you have downloaded

import zipfile 
import os
import shutil
DOWNLOAD_FOLDER = "C:\\Users\\maste\\Downloads\\"
PROJECT_DATA_FOLDER = "C:\\Users\\maste\\source\\repos\\Sztuczna inteligencja\\Weather_Prediction\\data\\"
YEAR_START = 1966
YEAR_END = 1997
indexes = ["140", "205", "295", "375", "424", "600"]

for year in range (YEAR_START, YEAR_END, 5):
    for index in indexes:
        path = DOWNLOAD_FOLDER + str(year) + "_" + str(year+4) + "_" + index+ "_s.zip"
        print(path)
        if not os.path.exists(path):
            break
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(DOWNLOAD_FOLDER)
        fileToDelete = DOWNLOAD_FOLDER +"s_d_t_"+index+"_"+ str(year) + "_" + str(year+4) + ".csv"
        if index == "155" and not os.path.exists(fileToDelete):
            fileToDelete = DOWNLOAD_FOLDER +"s_d_t_140_"+ str(year) + "_" + str(year+4) + ".csv"
            if not os.path.exists(fileToDelete):
                fileToDelete = DOWNLOAD_FOLDER +"s_d_t_150_"+ str(year) + "_" + str(year+4) + ".csv"
        
        os.remove(fileToDelete)
        os.remove(path)

    for index in indexes:
        
        newPath = PROJECT_DATA_FOLDER + str(year) + "_" + str(year+4) 
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        file = "s_d_" + index + "_" + str(year) + "_" + str(year+4) + ".csv"
        
        oldPath = DOWNLOAD_FOLDER + file
        if index == "155" and not os.path.exists(oldPath):
            file = "s_d_140_" + str(year) + "_" + str(year+4) + ".csv"
            oldPath = DOWNLOAD_FOLDER + file
            if not os.path.exists(oldPath):
                file = "s_d_150_" + str(year) + "_" + str(year+4) + ".csv"
                oldPath = DOWNLOAD_FOLDER + file
        if not os.path.exists(newPath+"\\"+file) and os.path.exists(oldPath):
            shutil.move(oldPath, newPath)
        else:
            if os.path.exists(oldPath):
                os.remove(oldPath)
            