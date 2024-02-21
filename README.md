# Digi-Dynamics
**Name**: Steam Scout 


# Prereqs
- Python version: 3.12
- Django==5.0.1
- beautifulsoup4==4.12.3
- python-steam-api==1.2.2
- mysql-connector-python==8.3.0
- mySQL: https://dev.mysql.com/downloads/file/?id=526407 

Install all prereqs (except mySQL, that needs to be done through the URL)
```
py -m pip install -r requirements.txt
```

or 
Install Individually
```
py -m pip install <package>
```

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
<a href="https://docs.djangoproject.com/en/5.0/">https://docs.djangoproject.com/en/5.0/ </a>

1) change curr directory:

``` 
cd mysite 
```
2) Run django **(START HERE when you pull this code)**
  ```
  py manage.py runserver
  ```
  or 
  ```
  py -m manage runserver
  ```
4) Put this URL into the page:
  <a href = "http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>

5) Note: if you need any help with finding a command, use
```
py manage.py --help
```
or 
```
py -m manage --help
```

Access admin webpage using <a href="http://127.0.0.1:8000/admin/">http://127.0.0.1:8000/admin/</a>
# TODO
- [ ] Apply steam web API with a database
- [X] Figure out the schema of steam game market
- [ ] Use Django in order to build a website
- [ ] Django has a built in database we can use if need be (Note: Optional can use other databases if need be)
- [ ] 

# Done
- [x] Decide On Final Project Plan
- [x] Added a steam web API
- [x] Saw templates on how each APICall works within APICalls/

# Types from steam web API
<ul>
  <li>Game</li>
  <li>Music</li>
  <li>Demo</li>
  <li>DLC</li>
</ul>

# Database
<b>Game Schema</b>
- Type
- Name
- SteamAppID
- Support Info
- DLC ("dlc")
- Base_price
- Current_Price
- Developer 
- Publisher
- Genre
- Release_data
- Top Seller
- ControllerSupport
- Image
- Highlight
- Trailer
- Age Requirement
- Platform ("platforms")
- languages ("supported languages") 
- tags ("categories") 
- Detailed Description
- Short Description
- Website


<b>Music Schema</b>
- Name
- Base_price
- Current_Price
- Developer 
- Publisher
- Release_data
- ControllerSupport
- Image
- SteamAppID
- Support Info
- Website
- Detailed Description
- Short Description
- Age Requirement
- Platform ("platforms")
- languages ("supported languages")

<b>DLC Schema</b>

- Name
- Base_price
- Current_Price
- Developer 
- Publisher
- Release_data
- ControllerSupport
- Image
- SteamAppID
- Support Info
- Website
- Detailed Description
- Short Description
- Age Requirement
- Platform ("platforms")
- languages ("supported languages") 
- tags ("categories") 


<b>Demo Schema</b>
- SteamAppID
- Support Info
- Name
- Base_price
- Current_Price
- Developer 
- Publisher
- Release_data
- Images
- Website
- Age Requirement
- Detailed Description
- Short Description
- Platform ("platforms")
- languages ("supported languages") 
- tags ("categories") 


<b>Movie Schema</b>
- SteamAppID (foreign key)
- Support Info
- Highlight
- Trailer
- 480p
- "max" resolution


- Note: Any thing with a * may be an issue 

```
PrimaryKey: SteamAppID
ForeignKey: ?
```
# Project Idea
- [x] Steam Game Search Engine


# credit
**Collaborators**:  
- Hunter Smith
- Alfred Newsome
- Isaac Watts
- Tamia