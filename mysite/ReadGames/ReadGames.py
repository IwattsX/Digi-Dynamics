# python file for reading all the games inside of Games folder and putting it into a dictionary

import json 
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

GamesDir = f"{BASE_DIR}/Games"



# print(GamesDir)



dictTypes = {
    "game" : 0,
    "music" : 0,
    "dlc" : 0,
    "demo" : 0,
}
for file in os.listdir(GamesDir):
    filePath = f"{GamesDir}/{file}"
    with open(filePath, 'r') as inputFile:
        temp = json.load(inputFile)
        typeOfJSON = temp['type']
        dictTypes[temp['type']] += 1
        print(temp['name'])
        print(typeOfJSON)



print(dictTypes)
