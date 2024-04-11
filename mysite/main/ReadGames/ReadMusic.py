from bs4 import BeautifulSoup
from database.InsertIntoSteam import Music
import os
import json
from pathlib import Path

# from pprint import pprint


def Music_Handler(Music : dict):
    # pprint(Music)
    music_res = dict()
    Elements = ["steam_appid","name", "support_info", 
                "price_overview", "developers", "publishers", 
                "release_date", "required_age", "website", "short_description", 
                "detailed_description", "supported_languages", "platforms", "header_image", 
                "controller_support", "fullgame"]
    for elem in Elements:
        music_val = Music.get(elem)

        if music_val:
            if elem == "price_overview":
                music_res["Base_price"] = music_val.get("initial", None)
                music_res["Current_price"] = music_val.get("final", None)
            
            elif elem == "fullgame":
                music_res[elem] = music_val.get("appid", None)

            elif elem == "developers":
                if len(music_val) == 1 and music_val[0] == '':
                    music_res[elem] = None
                else:
                    music_res[elem] = ", ".join(e for e in music_val)

            elif elem  == "publishers":
                if len(music_val) == 1 and music_val[0] == '':
                    music_res[elem] = None
                else:
                    music_res[elem] = ", ".join(e for e in music_val)
            
            elif elem == "genres":
                genres = [genre.get("description") for genre in music_val if genre]
                music_res[elem] = ", ".join(genres)

            elif elem == "release_date":
                coming_soon = music_val.get("coming_soon")
                date = music_val.get("date")

                music_res["coming_soon"] = coming_soon
                music_res['date'] = date

            elif elem == "platforms":
                music_res["windows"] = music_val.get("windows", False)
                music_res["linux"] = music_val.get("linux", False)
                music_res["mac"] = music_val.get("mac", False)

                # print(f"Windows: {game_res["windows"]}\nLinux: {game_res["linux"]}\nmac {game_res["mac"]}")
            elif elem == "support_info":
                music_res[elem] = music_val.get("email")
            
            elif elem == "steam_appid":
                # Need to convert the steam id to string not int when inserting into mySQL
                music_res[elem] = str(music_val)
            
            elif elem == "controller_support":
                music_res["controller_support"] = music_val
            
            elif elem in ["detailed_description", "short_description"]:
                soup = BeautifulSoup(music_val, features='html.parser')
                temp = ''.join(soup.stripped_strings)
                music_res[elem] = temp

            elif type(music_val) == str and "http" not in music_val:
                soup = BeautifulSoup(music_val, features='html.parser')
                temp = ''.join(soup.stripped_strings)
                music_res[elem] = temp

            else:
                music_res[elem] = music_val
    # pprint(music_res)
    return music_res

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

GamesDir = f"{BASE_DIR}/ReadGames/Data/music"

# print(GamesDir)

dictTypes = {
    "game" : 0,
    "music" : 0,
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

        if typeOfData == "music":
            Music_dict = Music_Handler(temp)


            Music(
                Music_dict.get("steam_appid"),
                Music_dict.get("name"),
                Music_dict.get("support_info"),
                Music_dict.get("Base_price"),
                Music_dict.get("Current_price"),
                Music_dict.get("developers"),
                Music_dict.get("publishers"),
                Music_dict.get("coming_soon"),
                Music_dict.get("date"),
                Music_dict.get("required_age"),
                Music_dict.get("controller_support"),
                Music_dict.get("website"),
                Music_dict.get("short_description"),
                Music_dict.get("detailed_description"),
                Music_dict.get("supported_languages"),
                Music_dict.get("windows"),
                Music_dict.get("linux"),
                Music_dict.get("mac"),
                Music_dict.get("header_image"),
                Music_dict.get("fullgame"),
            )

print(dictTypes)
