import requests
from decouple import config
import json
# Gets game info based off appids 
# NOTE: Using this for if the user types a game into the form, it will get the information if it isn't present in the database. 

def get_game_info(appid, api_key):
    # Get detailed information about a specific game
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

            with open("CODDLC.json", 'w') as outfile:
                json.dump(game_info, outfile, sort_keys=True, indent=4)

            print(f"Game: {game_info['name'].encode('utf-8')}")
            print(f"Developer(s): {', '.join(developer)}".encode('utf-8'))
            print(f"Publisher(s): {', '.join(publisher)}".encode('utf-8'))
            print("\n")
        else:
            print(f"Failed to retrieve data for appid {appid}")
    else:
        print(f"Failed to make the API request. Status code: {details_response.status_code}")

if __name__ == '__main__':
    KEY = config("STEAM_API_KEY")
    # get_game_info(1086940, KEY)
    # get_game_info(1938090, KEY)
    get_game_info(2053671, KEY)