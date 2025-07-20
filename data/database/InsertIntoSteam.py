from Connect_DB import connect
from pathlib import Path
import os
from sqlalchemy import text
from pprint import pprint
import json

from Handlers import Game_Handler, Music_Handler, DLC_Handler, Demo_Handler  # Make sure these exist



def insert_into_steam(query, args):
    engine = connect()
    print("Executing query:")
    pprint(args)
    with engine.begin() as conn:
        conn.execute(text(query), args)
    print("Finished the query with success")


def insert_handler(table_name, args):
    if table_name == "games":
        elements = ["steam_appid", "name", "support_info", "dlc", 
                    "Base_price", "Current_price", "developers", "publishers", "genres", 
                    "release_date", "required_age", "controller_support", "website", "short_description", 
                    "detailed_description", "supported_languages", "windows", "linux", "mac", "header_image"]
        passed_data = {elem: args.get(elem) for elem in elements}

        insert_into_steam("""
            INSERT INTO Games (
                id, Name, support_info, DLC, Base_price, Current_price, Developer,
                Publisher, Genre, release_date, Required_age, Controller_Support, Website,
                Short_description, Detailed_description, Supported_languages, windows, linux, mac, Header_image
            )
            VALUES (
                :steam_appid, :name, :support_info, :dlc, :Base_price, :Current_price, :developers,
                :publishers, :genres, :release_date, :required_age, :controller_support, :website,
                :short_description, :detailed_description, :supported_languages, :windows, :linux, :mac, :header_image
            )
            ON CONFLICT(id) DO NOTHING;
        """, passed_data)

    # elif table_name == "music":
    #     # Fill in the relevant fields and table structure
    #     insert_into_steam("""
    #         INSERT INTO Music (id, name, release_date, developer, publisher, header_image)
    #         VALUES (:steam_appid, :name, :release_date, :developers, :publishers, :header_image)
    #     """, {
    #         'steam_appid': args.get("steam_appid"),
    #         'name': args.get("name"),
    #         'release_date': args.get("release_date"),
    #         'developers': args.get("developers"),
    #         'publishers': args.get("publishers"),
    #         'header_image': args.get("header_image")
    #     })

    # elif table_name == "dlc":
    #     insert_into_steam("""
    #         INSERT INTO DLC (id, name, base_game_id, release_date)
    #         VALUES (:steam_appid, :name, :dlc_for_appid, :release_date)
    #     """, {
    #         'steam_appid': args.get("steam_appid"),
    #         'name': args.get("name"),
    #         'dlc_for_appid': args.get("dlc_for_appid"),
    #         'release_date': args.get("release_date")
    #     })

    # elif table_name == "demo":
    #     insert_into_steam("""
    #         INSERT INTO Demo (id, name, full_game_id, release_date)
    #         VALUES (:steam_appid, :name, :demo_for_appid, :release_date)
    #     """, {
    #         'steam_appid': args.get("steam_appid"),
    #         'name': args.get("name"),
    #         'demo_for_appid': args.get("demo_for_appid"),
    #         'release_date': args.get("release_date")
    #     })


if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parent.parent
    SORTED_DIR = BASE_DIR / 'sorted_games'

    directories = ["game", "demo", "dlc", "music"]
    for dir in directories:
        folder_path = SORTED_DIR / dir
        for file in os.listdir(folder_path):
            if file.endswith('.json'):
                filepath = folder_path / file
                try:
                    with open(filepath, 'r') as input_file:
                        tmp = json.load(input_file)
                        case = tmp.get('type')
                        if not case:
                            print(f"Skipping file {file}, no 'type' field found.")
                            continue

                        if case == 'game':
                            data_dict = Game_Handler(tmp)
                            insert_handler('games', data_dict)
                        elif case == 'music':
                            data_dict = Music_Handler(tmp)
                            insert_handler('music', data_dict)
                        elif case == 'dlc':
                            data_dict = DLC_Handler(tmp)
                            insert_handler('dlc', data_dict)
                        elif case == 'demo':
                            data_dict = Demo_Handler(tmp)
                            insert_handler('demo', data_dict)
                        else:
                            print(f"Unknown type '{case}' in file {file}")

                except Exception as e:
                    print(f"Error processing file {file}: {e}")
