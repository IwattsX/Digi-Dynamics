# python file for sorting Games into 4 different subsections

import os
from pathlib import Path
import shutil
import json


BASE_DIR = Path(__file__).resolve().parent.parent

GamesDir = f"{BASE_DIR}/Games"

Data_dir = f"{BASE_DIR}/ReadGames/Data"

for folder in ["game", "music", "dlc", "demo"]:
    folder_path = f"{Data_dir}/{folder}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

if __name__ == '__main__':
    for file in os.listdir(GamesDir):
        filePath = f"{GamesDir}/{file}"
        print(filePath)
        with open(filePath, 'r') as inputFile:
            temp = json.load(inputFile)
            typeOfData = temp['type']
            
            if typeOfData in ["game", "music", "dlc", "demo"]:
                if os.path.exists(f"{Data_dir}/{typeOfData}/{file}"):
                    print("This file has already been copied")
                else:
                    shutil.copy(filePath, f"{Data_dir}/{typeOfData}")