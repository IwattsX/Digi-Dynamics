from ReadGames import Game_Handler, movies_handler
from ReadMusic import Music_Handler
from ReadDLC import DLC_Handler
from ReadDemo import Demo_Handler

# Classes that auto insert into tables
from database.InsertIntoSteam import Games, Music, Movies


def Data_Handler(Data : dict):
    case = Data.get('type', None)
    if case == "game":
        Game_dict = Game_Handler(Data)
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
        
        
    elif case == "music":
        Music_dict = Music_Handler(Data)
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
          
    elif case == "dlc":
        # TODO: Implement this for dlc table
        pass
        DLC_Handler(Data)
     
    elif case == "demo":
        # TODO: Implement this in demo table
        Demo_Handler(Data)



# Automatically run code from these files
# NOTE: Read the games first as the others require that you have foreign keys to it
if __name__ == '__main__':
    import ReadGames
    import ReadMusic
    import ReadDLC
    import ReadDemo
