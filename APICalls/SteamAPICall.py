# Link to API documentation: https://pypi.org/project/python-steam-api/
# TODO: Figure out how to get API calls inside of a database

from steam import Steam
from decouple import config

# Getting key from the .env file
KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

print(steam.users.search_user("the12thchairman"))