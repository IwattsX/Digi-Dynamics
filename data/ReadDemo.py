from bs4 import BeautifulSoup
from database.InsertIntoSteam import Demo
import os
import json
from pathlib import Path

# from pprint import pprint


def Demo_Handler(Demo : dict):
    # pprint(Demo)
    Demo_res = dict()
    Elements = ["steam_appid","name", "support_info", 
                "developers", "publishers", 
                "release_date", "required_age", "website", "short_description", 
                "detailed_description", "supported_languages", "platforms", "header_image", 
                "controller_support", "fullgame"]
    for elem in Elements:
        Demo_val = Demo.get(elem)

        if Demo_val:            
            if elem == "fullgame":
                Demo_res[elem] = Demo_val.get("appid", None)

            elif elem == "developers":
                if len(Demo_val) == 1 and Demo_val[0] == '':
                    Demo_res[elem] = None
                else:
                    Demo_res[elem] = ", ".join(e for e in Demo_val)

            elif elem  == "publishers":
                if len(Demo_val) == 1 and Demo_val[0] == '':
                    Demo_res[elem] = None
                else:
                    Demo_res[elem] = ", ".join(e for e in Demo_val)
            
            elif elem == "genres":
                genres = [genre.get("description") for genre in Demo_val if genre]
                Demo_res[elem] = ", ".join(genres)

            elif elem == "release_date":
                coming_soon = Demo_val.get("coming_soon")
                date = Demo_val.get("date")

                Demo_res["coming_soon"] = coming_soon
                Demo_res['date'] = date

            elif elem == "platforms":
                Demo_res["windows"] = Demo_val.get("windows", False)
                Demo_res["linux"] = Demo_val.get("linux", False)
                Demo_res["mac"] = Demo_val.get("mac", False)

                # print(f"Windows: {game_res["windows"]}\nLinux: {game_res["linux"]}\nmac {game_res["mac"]}")
            elif elem == "support_info":
                Demo_res[elem] = Demo_val.get("email")
            
            elif elem == "steam_appid":
                # Need to convert the steam id to string not int when inserting into mySQL
                Demo_res[elem] = str(Demo_val)
            
            elif elem == "controller_support":
                Demo_res["controller_support"] = Demo_val
            
            elif elem in ["detailed_description", "short_description"]:
                soup = BeautifulSoup(Demo_val, features='html.parser')
                temp = ''.join(soup.stripped_strings)
                Demo_res[elem] = temp

            elif isinstance(Demo_val,str) and "http" not in Demo_val:
                soup = BeautifulSoup(Demo_val, features='html.parser')
                temp = ''.join(soup.stripped_strings)
                Demo_res[elem] = temp

            else:
                Demo_res[elem] = Demo_val
    # pprint(Demo_res)
    return Demo_res

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

GamesDir = f"{BASE_DIR}/ReadGames/Data/Demo"

# print(GamesDir)

for file in os.listdir(GamesDir):
    filePath = f"{GamesDir}/{file}"

    # print(filePath)
    with open(filePath, 'r') as inputFile:
        temp = json.load(inputFile)
        typeOfData = temp['type']

        if typeOfData == "demo":
            Demo_dict = Demo_Handler(temp)

            Demo(
                Demo_dict.get("steam_appid"),
                Demo_dict.get("name"),
                Demo_dict.get("support_info"),
                Demo_dict.get("developers"),
                Demo_dict.get("publishers"),
                Demo_dict.get("genres"),
                Demo_dict.get("date"),
                Demo_dict.get("required_age"),
                Demo_dict.get("controller_support"),
                Demo_dict.get("website"),
                Demo_dict.get("short_description"),
                Demo_dict.get("detailed_description"),
                Demo_dict.get("supported_languages"),
                Demo_dict.get("windows"),
                Demo_dict.get("linux"),
                Demo_dict.get("mac"),
                Demo_dict.get("header_image"),
                Demo_dict.get("fullgame"),
            )


            # Demo(
            #     Demo_dict.get("steam_appid"),
            #     Demo_dict.get("name"),
            #     Demo_dict.get("support_info"),
            #     Demo_dict.get("developers"),
            #     Demo_dict.get("publishers"),
            #     Demo_dict.get("coming_soon"),
            #     Demo_dict.get("date"),
            #     Demo_dict.get("required_age"),
            #     Demo_dict.get("controller_support"),
            #     Demo_dict.get("website"),
            #     Demo_dict.get("short_description"),
            #     Demo_dict.get("detailed_description"),
            #     Demo_dict.get("supported_languages"),
            #     Demo_dict.get("windows"),
            #     Demo_dict.get("linux"),
            #     Demo_dict.get("mac"),
            #     Demo_dict.get("header_image"),
            #     Demo_dict.get("fullgame")
            # )