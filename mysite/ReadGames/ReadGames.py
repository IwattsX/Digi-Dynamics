from bs4 import BeautifulSoup
import json 
import os
from pathlib import Path
from pprint import pprint
from database.InsertIntoSteam import Games


# Python file for handling all the date inside of the Games Folder

# All files have a "minimum" in them
# However PC_requirements seems to be the only thing that matters
# Both a minimum and a recommended
# Since steam is primarily for PC and we can just use linux: windows: and Mac: keys
# to determine if the game supports those OS's

"""
    Order of mySQL columns to not get confused
    id, Name, support_info, DLC, Base_price, 
    Curr_price, Developer, Publisher, Genres, Coming_soon, 
    Release_Date, Required_age, Controller_support, Website, Short_description, 
    Detailed_description, Supported_languages, PLATFORM, Header_image

    Will need to convert most of this to string
    DLC is of type list but convert to a string using 

    Note if sometimes price_overview is NULL, so assume either it is 0 or "coming soon" and possibly doesn't have a price yet

    Base_price = price_overview.initial
    current_price = price_overview.final

    Developers and Publishers are list types

    Genres will be a list type

    release_date and Coming Soon under:
    release_date['date']
    release_date['coming_soon']

    platforms.x
    x = 
    windows: ... BOOL
    linux: ...
    mac: ...

    header_image


    NOTE: Most of these things need a BeutifulSoup HTML.parser


"""


def Game_Handler(game : dict):
    # Only elements we care about for the most part
    game_res = dict()


    Elements = ["steam_appid","name", "support_info", "dlc", 
                "price_overview", "developers", "publishers", "genres", 
                "release_date", "required_age", "website", "short_description", 
                "detailed_description", "supported_languages", "platforms", "header_image", 
                "controller_support"]
    
    for elem in Elements:
        game_val = game.get(elem)

        if game_val:
            if elem == "price_overview":
                game_res["Base_price"] = game_val.get("initial", None)
                game_res["Current_price"] = game_val.get("final", None)
            
            elif elem in ["developers", "publishers"]:
                game_res[elem] = ", ".join(e for e in game_val)
            
            elif elem == "genres":
                genres = [genre.get("description") for genre in game_val if genre]
                game_res[elem] = ", ".join(genres)

            elif elem == "release_date":
                coming_soon = game_val.get("coming_soon")
                date = game_val.get("date")

                game_res["coming_soon"] = coming_soon
                game_res['date'] = date

            elif elem == "platforms":
                game_res["windows"] = game_val.get("windows", False)
                game_res["linux"] = game_val.get("linux", False)
                game_res["mac"] = game_val.get("mac", False)

                # print(f"Windows: {game_res["windows"]}\nLinux: {game_res["linux"]}\nmac {game_res["mac"]}")
            elif elem == "support_info":
                game_res[elem] = game_val.get("email")
            
            elif elem == "steam_appid":
                # Need to convert the steam id to string not int when inserting into mySQL
                game_res[elem] = str(game_val)
            
            elif elem == "controller_support":
                game_res["controller_support"] = game_val
            elif elem in ["detailed_description", "short_description"]:
                soup = BeautifulSoup(game_val, features='html.parser')
                temp = ''.join(soup.stripped_strings)
                game_res[elem] = temp

            elif type(game_val) == str and "http" not in game_val:
                soup = BeautifulSoup(game_val, features='html.parser')
                temp = ''.join(soup.stripped_strings)
                game_res[elem] = temp
            
            elif elem == 'dlc':
                DLCs = [str(dlc) for dlc in game_val]
                game_res[elem] = ", ".join(DLCs)
            
            else:
                game_res[elem] = game_val    
    # pprint(game_res)
    return game_res

    


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


# Handle all incoming data from the API
def Data_Handler(Data : dict):
    case = Data.get('type', None)
    if case == "game":
        Game_Handler(Data)
        
    elif case == "music":
        Music_Handler(Data)
          
    elif case == "dlc":
        DLC_Handler(Data)
     
    elif case == "demo":
        Demo_Handler(Data)


if __name__ == '__main__':
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

        print(filePath)
        with open(filePath, 'r') as inputFile:
            temp = json.load(inputFile)
            typeOfData = temp['type']
            dictTypes[temp['type']] += 1

            if typeOfData == "game":
                Game_dict = Game_Handler(temp)

                insert_this = Games(
                    Game_dict.get('steam_appid'),
                    Game_dict.get('name'),
                    Game_dict.get('support_info'),
                    Game_dict.get('dlc'), 
                    Game_dict.get('Base_price'),
                    Game_dict.get("Current_price"),
                    Game_dict.get("developers"),
                    Game_dict.get("publishers"),
                    Game_dict.get("genres"),
                    Game_dict.get("coming_soon"),
                    Game_dict.get('date'),
                    Game_dict.get("required_age"),
                    Game_dict.get("controller_support"),
                    Game_dict.get("website"),
                    Game_dict.get("short_description"),
                    Game_dict.get("detailed_description"),
                    Game_dict.get("supported_languages"),
                    Game_dict.get("windows"),
                    Game_dict.get("linux"),
                    Game_dict.get("mac"),
                    Game_dict.get("header_image")
                )

                
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