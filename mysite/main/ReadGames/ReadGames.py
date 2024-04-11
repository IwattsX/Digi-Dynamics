from bs4 import BeautifulSoup
import json 
import os
from pathlib import Path
from database.InsertIntoSteam import Games, Music, Movies

# comment this out when we won't use it anymore for debugging
from pprint import pprint

# Python file for handling all the date inside of the Games Folder

# For trailers or how steam calls it "Movies"
# TODO: Make this work with the Games_Hander for the Movies Data

"""
            %(id)s,
            %(name)s,
            %(thumbnail)s,
            %(mp4_480p)s,
            %(mp4_max)s,
            %(webm_480p)s,
            %(webm_max)s,
            %(game_ID)s"""


def movies_handler(movie : dict) -> dict:
    movie_res = dict()
    if not movie:
        return movie_res
    
    Elements = ["id", "name", "thumbnail", "mp4", "webm"]
    for trailer in movie:
        for elem in Elements:
            movie_val = trailer.get(elem, None)
            if movie_val:
                if elem == 'mp4' or elem == 'webm':
                    movie_res[elem + "_480p"] = movie_val.get("480", None)
                    movie_res[elem + "_max"] = movie_val.get("max", None)
                else:
                    movie_res[elem] = movie_val
    return movie_res


def Game_Handler(game : dict):
    # Only elements we care about for the most part
    game_res = dict()


    Elements = ["steam_appid","name", "support_info", "dlc", 
                "price_overview", "developers", "publishers", "genres", 
                "release_date", "required_age", "website", "short_description", 
                "detailed_description", "supported_languages", "platforms", "header_image", 
                "controller_support", "movies"]
    
    for elem in Elements:
        game_val = game.get(elem)

        if game_val:
            if elem == "movies":
                game_res[elem] = game_val
            if elem == "price_overview":
                game_res["Base_price"] = game_val.get("initial", None)
                game_res["Current_price"] = game_val.get("final", None)
            
            elif elem == "developers":
                if len(game_val) == 1 and game_val[0] == '':
                    game_res[elem] = None
                else:
                    game_res[elem] = ", ".join(e for e in game_val)

            elif elem  == "publishers":
                if len(game_val) == 1 and game_val[0] == '':
                    game_res[elem] = None
                else:
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

def DLC_Handler(DLC:dict):
    for k, v in DLC.items():
        print(k)
        print(v)
        print("------------------------")


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
            
            elif elem == 'dlc':
                DLCs = [str(dlc) for dlc in music_val]
                music_res[elem] = ", ".join(DLCs)
            
            else:
                music_res[elem] = music_val
    # pprint(music_res)
    return music_res


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
    
    # # edge case when the Steam Web API gives me a type movie
    # elif case == "movie":
    #     Movie_Handler(Data)


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

        # print(filePath)
        with open(filePath, 'r') as inputFile:
            temp = json.load(inputFile)
            typeOfData = temp['type']
            dictTypes[temp['type']] += 1

            if typeOfData == "game":
                Game_dict = Game_Handler(temp)
                Games(
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
                movies_dict = movies_handler(Game_dict.get("movies"))
                if not movies_dict.get("id") is None:

                    Movies(
                        movies_dict.get("id"),
                        movies_dict.get("name"),
                        movies_dict.get("thumbnail"),
                        movies_dict.get("mp4_480p"),
                        movies_dict.get("mp4_max"),
                        movies_dict.get("webm_480p"),
                        movies_dict.get("webm_max"),
                        Game_dict.get("steam_appid"),
                    )
                
            elif typeOfData == "music":
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

            elif typeOfData == "dlc":
                continue
                DLC_Handler(temp)


            
            
            elif typeOfData == "demo":
                continue
                Demo_Handler(temp)


                

            # print(temp['name'])
            # print(typeOfData)

    print(dictTypes)
