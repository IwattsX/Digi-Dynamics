# python file for reading all the games inside of Games folder and putting it into a dictionary


from bs4 import BeautifulSoup
import json 
import os
from pathlib import Path
from pprint import pprint
# All files have a "minimum" in them
# However PC_requirements seems to be the only thing that matters
# Both a minimum and a recommended
# Since steam is primarily for PC and we can just use linux: windows: and Mac: keys
# to determine if the game supports those OS's



    
game_number = 0


def Game_Handler(game : dict):
    # Only elements we care about for the most part
    game_res = dict()

    Elements = ["about_the_game", "pc_requirements", "short_description"]

    for elem in Elements:
        game_elem = game.get(elem)
        if game_elem:
            if "requirements" in elem:
                MinSoup = BeautifulSoup(game_elem.get('minimum', ""), features='html.parser')
                recommended = BeautifulSoup(game_elem.get('recommended', ""), features='html.parser')

                minSoupStr = ' '.join(MinSoup.stripped_strings)
                recommendedStr = ' '.join(recommended.stripped_strings)

                game_res[elem] = {
                    "minimum": minSoupStr,
                    "recommended" : recommendedStr
                }
            else:
                soup = BeautifulSoup(game.get(elem, None), features='html.parser')
                temp = ' '.join(soup.stripped_strings)
                game_res[elem] = temp
        pprint(game_res)

    


    # game_number += 1
    # for elem in Elements:
    #     print(game_number)
    #     if game.get(elem):
    #         print(game[elem])
    #     else:
    #         print("THIS IS A NONETYPE")
        

    # soup  = BeautifulSoup(game.get("about_the_game", "Nothing here"),"html.parser")
    # text_without_code = "".join(soup.stripped_strings)
    # game["about_the_game"] = text_without_code
    # for k, v in game.items():
    #     print(k)
    #     print("------------------------")

def DLC_Handler(DLC:dict):
    for k, v in DLC.items():
        print(k)
        print(v)
        print("------------------------")

def Music_Handler(Music : dict):
    for k, v in Music.items():
        print(k)
        print(v)
        print("------------------------")

def Demo_Handler(Demo: dict):
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
            break
            
        elif typeOfData == "music":
            continue
            Music_Handler(temp)
            
        
        elif typeOfData == "dlc":
            continue
            DLC_Handler(temp)
        
        
        elif typeOfData == "demo":
            continue
            Demo_Handler(temp)
            

        # print(temp['name'])
        # print(typeOfData)



print(dictTypes)
