# python file for reading all the games inside of Games folder and putting it into a dictionary

import json 
import os
from pathlib import Path

def Game_Handler(game : dict()):
    for k, v in game.items():
        print(k)
        print(v)
        print("------------------------")

def DLC_Handler(DLC:dict()):
    for k, v in DLC.items():
        print(k)
        print(v)
        print("------------------------")

def Music_Handler(Music : dict()):
    for k, v in Music.items():
        print(k)
        print(v)
        print("------------------------")

def Demo_Handler(Demo: dict()):
    for k, v in Demo.items():
        print(k)
        print(v)
        print("------------------------")


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
        typeOfData = temp['type']
        dictTypes[temp['type']] += 1

        if typeOfData == "game":
            Game_Handler(temp)
            
        elif typeOfData == "music":
            Music_Handler(temp)
            
        
        elif typeOfData == "dlc":
            DLC_Handler(temp)
        
        
        elif typeOfData == "demo":
            Demo_Handler(temp)
            

        # print(temp['name'])
        # print(typeOfData)



print(dictTypes)
