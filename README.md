# Digi-Dynamics
**Name**: Steam Scout 
**Collaborators**:  
- Hunter Smith
- Alfred Newsome
- Isaac Watts
- Tamia

# HOW TO RUN
<a href="https://docs.djangoproject.com/en/5.0/">https://docs.djangoproject.com/en/5.0/ </a>

1) Check version:
  ```
  python -m django --version
  ```
2) Use Django to start a project
  ```
  django-admin startproject mysite
  ```
  or if that doesn't work use  
  ```
  python -m django-admin startproject mysite
  ```
3) Run django **(START HERE when you pull this code)**
  ```
  python manage.py runserver
  ```
  or 
  ```
  py -m manage runserver
  ```
4) Put this URL into the page:
  <a href = "http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>

5) Note: if you need any help with finding a command, use
```
python manage.py --help
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
<table>
  <tr>

    -Type
    -Name
    -SteamAppID
    -Support Info
    -DLC ("dlc")
    -Base_price
    -Current_Price
    -Developer 
    -Publisher
    -Genre
    -Release_data
    -Top Seller
    -ControllerSupport
    -Image
    -Highlight
    -Trailer
    -Age Requirement
    -Platform ("platforms")
    -languages ("supported languages") 
    -tags ("categories") 
    -Detailed Description
    -Short Description
    -Website
  </tr>
</table>

<b>Music Schema</b>

<table>
  <tr>

    -Name
    -Base_price
    -Current_Price
    -Developer 
    -Publisher
    -Release_data
    -ControllerSupport
    -Image
    -SteamAppID
    -Support Info
    -Website
    -Detailed Description
    -Short Description
    -Age Requirement
    -Platform ("platforms")
    -languages ("supported languages")
  </tr>
</table>

<b>DLC Schema</b>

<table>
  <tr>

    -Name
    -Base_price
    -Current_Price
    -Developer 
    -Publisher
    -Release_data
    -ControllerSupport
    -Image
    -SteamAppID
    -Support Info
    -Website
    -Detailed Description
    -Short Description
    -Age Requirement
    -Platform ("platforms")
    -languages ("supported languages") 
    -tags ("categories") 
  </tr>
</table>

<b>Demo Schema</b>

<table>
  <tr>

    -SteamAppID
    -Support Info
    -Name
    -Base_price
    -Current_Price
    -Developer 
    -Publisher
    -Release_data
    -Images
    -Website
    -Age Requirement
    -Detailed Description
    -Short Description
    -Platform ("platforms")
    -languages ("supported languages") 
    -tags ("categories") 

  </tr>
</table>

<b>Movie Schema</b>

<table>
  <tr>

    -SteamAppID (foreign key)
    -Support Info
    -Highlight
    -Trailer
    -480p
    -"max" resolution

  </tr>
</table>
- Note: Any thing with a * may be an issue 

```
PrimaryKey: SteamAppID
ForeignKey: ?
```
# Project Ideas
- [x] Steam Game Search Engine

# Dependencies
- Django==5.0.1
- beautifulsoup4==4.12.3
- python-steam-api==1.2.2
- mySQL: https://dev.mysql.com/downloads/file/?id=526407 
