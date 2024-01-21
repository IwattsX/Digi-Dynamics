# -*- coding: utf-8 -*-

import requests
import json

from decouple import config

# Replace 'YOUR_API_KEY' with the actual API key you obtained

KEY = config("STEAM_API_KEY")

api_key = KEY
steam_api_url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'

# Step 2: Get the list of all games on Steam
response = requests.get(steam_api_url)
app_list = response.json()['applist']['apps']
i = 0

# Step 3: Iterate through the list of games
for app in app_list:
    appid = app['appid']

    # Step 4: Get detailed information about a specific game
    app_details_url = f'http://store.steampowered.com/api/appdetails?appids={appid}&key={api_key}'
    details_response = requests.get(app_details_url)
    details_data = details_response.json()

    # Extract developer and publisher information
    if details_data.get(str(appid)) and details_data[str(appid)]['success']:
        game_info = details_data[str(appid)]['data']
        developer = game_info.get('developers', [])
        publisher = game_info.get('publishers', [])
        i += 1

        with open(f"Samples/sample{i}.json", "w") as outfile: 
            json.dump(game_info, outfile)
        
        print("----------------")
        # print(f"Game: {game_info['name']}")
        print(f"Developer(s): {', '.join(developer)}".encode('utf-8'))
        print(f"Publisher(s): {', '.join(publisher)}".encode('utf-8'))
        print("\n")
