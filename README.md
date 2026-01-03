# Digi-Dynamics
**Name**: Steam Scout 


# Prereqs
- Python version: 3.12
- python-decouple==3.8
- Django==5.0.1
- beautifulsoup4==4.12.3
- python-steam-api==1.2.2
- mysql-connector-python==8.3.0
- mySQL: https://dev.mysql.com/downloads/file/?id=526407 or install Xampp


NOTE: You are going to have to create 2 .env files in mysite/APICalls and mysite/database

mysite/APICalls/.env
```
STEAM_API_KEY= "<YOUR_API_KEY>"
```
Get this from <a href="https://steamcommunity.com/dev/apikey">https://steamcommunity.com/dev/apikey</a>


mysite/ReadGames/database/.env
```
uname = "<Your_Uname>"
pass = "<your_pass>"
database = "steam"
```

Note: uname will run the SQL through 'uname'@'localhost', I named my database "steam" 


# HOW TO RUN
Using uv:
```
uv run mysite/manage.py runserver
```
<a href="https://docs.djangoproject.com/en/5.0/">https://docs.djangoproject.com/en/5.0/ </a>
Access admin webpage using <a href="http://127.0.0.1:8000/admin/">http://127.0.0.1:8000/admin/</a>


# Types from steam web API
<ul>
  <li>Game</li>
  <li>Music</li>
  <li>Demo</li>
  <li>DLC</li>
</ul>

# Database Tables
<b>Games</b>
![alt "Games Table"](./descTables/Games.png)

<b>Music Schema</b>
![alt "Music Table"](./descTables/Music.png)

<b>DLC Schema</b>
![alt "DLC Table"](./descTables/DLC.png)

<b>Demo Schema</b>
![alt "Demo Table"](./descTables/Demo.png)

<b>Movie Schema</b>
![alt "Music Table"](./descTables/Movies.png)


# Project Idea
- [x] Steam Game Search Engine


# credit
**Collaborators**:  
- Hunter Smith
- Alfred Newsome
- Isaac Watts
- Tamia
