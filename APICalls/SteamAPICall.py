# Use a .env file to use this
# python SteamAPICall.py > fileName.txt is how I ran it

# Getting the steam web API : https://steamcommunity.com/dev 
# Link to API documentation: https://pypi.org/project/python-steam-api/
# TODO: Figure out how to get API calls inside of a database

from steam import Steam
from decouple import config
import json


# Getting key from the .env file
KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

# print(steam.users.search_user("the12thchairman"))
games = steam.apps.search_games("terr")
with open("Terr.json", 'w') as outfile:
    json.dump(games, outfile, sort_keys=True, indent=4)

#This helped get the data and put it in a file. This is a Terraria example.
# NOTE: You can use part of the game names to get the data for all the games that have that prefix