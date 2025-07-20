from bs4 import BeautifulSoup
import json 
import os
from pathlib import Path


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

        if game_val is None:
            game_res[elem] = None
            continue
        
        if elem == "movies":
            game_res[elem] = json.dumps(game_val)
            
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
            game_res['release_date'] = date

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
        
        elif isinstance(game_val, str) and "http" not in game_val and ("<" in game_val and ">" in game_val):
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



def DLC_Handler(DLC : dict):
    DLC_res = dict()

    Elements = ["steam_appid","name", "support_info",
            "price_overview", "developers", "publishers", "genres", 
            "release_date", "required_age", "website", "short_description", 
            "detailed_description", "supported_languages", "platforms", "header_image", 
            "controller_support", "fullgame"]
    for elem in Elements:
        DLC_val = DLC.get(elem)

        if DLC_val is None:
            DLC_res[elem] = None
            continue

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

        if Demo_val is None:
            Demo_res[elem] = None
            continue
        
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

        if music_val is None:
            music_res[elem] = music_val
            continue

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