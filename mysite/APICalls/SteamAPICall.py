# Use a .env file to use this
# python SteamAPICall.py > fileName.txt is how I ran it

# Getting the steam web API : https://steamcommunity.com/dev 
# Link to API documentation: https://pypi.org/project/python-steam-api/
# TODO: Figure out how to get API calls inside of a database

from steam import Steam
from decouple import config
import requests
import json
from pprint import pprint

# Getting key from the .env file
KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

def get_game_info(appid, api_key) -> dict:
    # Get detailed information about a specific game
    res = dict()


    app_details_url = f'http://store.steampowered.com/api/appdetails?appids={appid}&key={api_key}'
    details_response = requests.get(app_details_url)

    # Check if the request was successful (status code 200)
    if details_response.status_code == 200:
        details_data = details_response.json()

        # Check if the expected data is present
        if details_data and details_data.get(str(appid)) and details_data[str(appid)].get('success'):
            game_info = details_data[str(appid)]['data']
            developer = game_info.get('developers', [])
            publisher = game_info.get('publishers', [])

            with open(f"game{appid}.json", 'w') as outfile:
                json.dump(game_info, outfile, sort_keys=True, indent=4)

            print(f"Game: {game_info['name'].encode('utf-8')}")
            print(f"Developer(s): {', '.join(developer)}".encode('utf-8'))
            print(f"Publisher(s): {', '.join(publisher)}".encode('utf-8'))
            print("\n")
            res = game_info
        else:
            print(f"Failed to retrieve data for appid {appid}")
    else:
        print(f"Failed to make the API request. Status code: {details_response.status_code}")
    return res
    


# print(steam.users.search_user("the12thchairman"))
def search_by_name(name : str):
    games = steam.apps.search_games(name)

    app = games.get('apps', None)
    if app:
        print("If statemente ran")
        for elem in app:
            id_str = ' '.join(str(id) for id in elem.get('id'))
            print("fetching game info for: " , id_str)
            final_games_dict = get_game_info(id_str, KEY)
            print("Success")
            # More logic to come here

    # pprint(games)
    # print(type(games))
    # print("-------------")
    # for k, v in games.items():
    #     print(k)
    #     print(type(k))
    #     print(v)
    #     print(type(v))

    return games

# games = steam.apps.search_games("terr")
# with open("Terr.json", 'w') as outfile:
#     json.dump(games, outfile, sort_keys=True, indent=4)

#This helped get the data and put it in a file. This is a Terraria example.
# NOTE: You can use part of the game names to get the data for all the games that have that prefix
    
if __name__ == '__main__':
    search_by_name("terr")