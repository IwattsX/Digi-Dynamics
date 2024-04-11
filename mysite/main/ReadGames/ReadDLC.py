from bs4 import BeautifulSoup
from database.InsertIntoSteam import DLC
import os
import json
from pathlib import Path

def DLC_Handler(DLC : dict):
    Elements = ["steam_appid","name", "support_info",
                "price_overview", "developers", "publishers", "genres", 
                "release_date", "required_age", "website", "short_description", 
                "detailed_description", "supported_languages", "platforms", "header_image", 
                "controller_support", "fullgame"]
    DLC_res = dict()
    for elem in Elements:
        DLC_val = DLC.get(elem)

        if DLC_val:
            if elem == "price_overview":
                DLC_res["Base_price"] = DLC_val.get("initial", None)
                DLC_res["Current_price"] = DLC_val.get("final", None)
            
            elif elem == "developers":
                if len(DLC_val) == 1 and DLC_val[0] == '':
                    DLC_res[elem] = None
                else:
                    DLC_res[elem] = ", ".join(e for e in DLC_val)
            
            elif elem == "fullgame":
                DLC_res[elem] = DLC_val.get("appid", None)

            elif elem  == "publishers":
                if len(DLC_val) == 1 and DLC_val[0] == '':
                    DLC_res[elem] = None
                else:
                    DLC_res[elem] = ", ".join(e for e in DLC_val)
            
            elif elem == "genres":
                genres = [genre.get("description") for genre in DLC_val if genre]
                DLC_res[elem] = ", ".join(genres)

            elif elem == "release_date":
                coming_soon = DLC_val.get("coming_soon")
                date = DLC_val.get("date")

                DLC_res["coming_soon"] = coming_soon
                DLC_res['date'] = date

            elif elem == "platforms":
                DLC_res["windows"] = DLC_val.get("windows", False)
                DLC_res["linux"] = DLC_val.get("linux", False)
                DLC_res["mac"] = DLC_val.get("mac", False)

                # print(f"Windows: {game_res["windows"]}\nLinux: {game_res["linux"]}\nmac {game_res["mac"]}")
            elif elem == "support_info":
                DLC_res[elem] = DLC_val.get("email")
            
            elif elem == "steam_appid":
                # Need to convert the steam id to string not int when inserting into mySQL
                DLC_res[elem] = str(DLC_val)
            
            elif elem == "controller_support":
                DLC_res["controller_support"] = DLC_val
            
            elif elem in ["detailed_description", "short_description"]:
                soup = BeautifulSoup(DLC_val, features='html.parser')
                temp = ''.join(soup.stripped_strings)
                DLC_res[elem] = temp

            elif type(DLC_val) == str and "http" not in DLC_val:
                soup = BeautifulSoup(DLC_val, features='html.parser')
                temp = ''.join(soup.stripped_strings)
                DLC_res[elem] = temp
            
            else:
                DLC_res[elem] = DLC_val
    # pprint(game_res)
    return DLC_res

BASE_DIR = Path(__file__).resolve().parent.parent

GamesDir = f"{BASE_DIR}/ReadGames/Data/dlc"

# print(GamesDir)

dictTypes = {
    "game" : 0,
    "dlc" : 0,
    "dlc" : 0,
    "demo" : 0,
}

for file in os.listdir(GamesDir):
    filePath = f"{GamesDir}/{file}"

    # print(filePath)
    with open(filePath, 'r') as inputFile:
        temp = json.load(inputFile)
        typeOfData = temp['type']
        dictTypes[temp['type']] += 1

        if typeOfData == "dlc":
            dlc_dict = DLC_Handler(temp)


            DLC(
                    dlc_dict.get('steam_appid'),
                    dlc_dict.get('name'),
                    dlc_dict.get('support_info'),
                    dlc_dict.get('Base_price'),
                    dlc_dict.get("Current_price"),
                    dlc_dict.get("developers"),
                    dlc_dict.get("publishers"),
                    dlc_dict.get("genres"),
                    dlc_dict.get("coming_soon"),
                    dlc_dict.get('date'),
                    dlc_dict.get("required_age"),
                    dlc_dict.get("controller_support"),
                    dlc_dict.get("website"),
                    dlc_dict.get("short_description"),
                    dlc_dict.get("detailed_description"),
                    dlc_dict.get("supported_languages"),
                    dlc_dict.get("windows"),
                    dlc_dict.get("linux"),
                    dlc_dict.get("mac"),
                    dlc_dict.get("header_image"),
                    dlc_dict.get("fullgame")
            )

print(dictTypes)