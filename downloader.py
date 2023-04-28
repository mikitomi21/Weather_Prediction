import requests
import os

indexes = ["205", "375", "600", "295", "424", "155"]
DOWNLOAD_FOLDER = "C:\\Users\\maste\\Downloads\\"

for year in range(1966, 1997, 5):
    for index in indexes:
        url = "https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/synop/" + str(year) + "_" + str(year+4)+ "/" + str(year) + "_" + str(year+4) + "_" + index + "_s.zip"
        response = requests.get(url)
        if not os.path.exists(DOWNLOAD_FOLDER+str(year)+"_"+index+"_s.zip"):
            open(DOWNLOAD_FOLDER + str(year) + "_" + str(year+4)+"_"+index+"_s.zip", "wb").write(response.content)
        
