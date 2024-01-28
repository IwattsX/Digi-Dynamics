# Digi-Dynamics
**Name**: Steam Scout <br>
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
  <a href = "http://127.0.0.1:8000/"><br>http://127.0.0.1:8000/</a>

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
    <th>Type</th>
    <th>Name</th>
    <th>SteamAppID<th>
    <th>Support Info<th>
    <th>DLC ("dlc")</th>
    <th>Microtransations</th>
    <th>Subsriptions</th>
    <th>Franchise</th>
    <th>Base_price</th>
    <th>Current_Price</th>
    <th>Country</th>
    <th>Developer </th>
    <th>Publisher</th>
    <th>Genre</th>
    <th>Rating</th>
    <th>Review</th>
    <th>Release_data</th>
    <th>Top Seller</th>
    <th>ControllerSupport</th>
    <th>Image</th>
    <th>Highlight</th>
    <th>Trailer</th>
    <th>Age Requirement</th>
    <th>Platform ("platforms")</tr>
    <th>languages ("supported languages") </th>
    <th>tags ("categories") </th>
    <th>Detailed Description</th>
    <th>Short Description</th>
    <th>Website<th>
  </tr>
</table>
<br><br>
<b>Music Schema</b>
<table>
  <tr>
    <th>Name</th>
    <th>Base_price</th>
    <th>Current_Price</th>
    <th>Developer </th>
    <th>Publisher</th>
    <th>Release_data</th>
    <th>ControllerSupport</th>
    <th>Image</th>
    <th>SteamAppID<th>
    <th>Support Info<th>
    <th>Website<th>
    <th>Detailed Description<th>
    <th>Short Description<th>
    <th>Age Requirement</th>
    <th>Platform ("platforms")</tr>
    <th>languages ("supported languages") </th>
  </tr>
</table>
<br><br>
<b>DLC Schema</b>
<table>
  <tr>
    <th>Name</th>
    <th>Base_price</th>
    <th>Current_Price</th>
    <th>Developer </th>
    <th>Publisher</th>
    <th>Release_data</th>
    <th>ControllerSupport</th>
    <th>Image</th>
    <th>SteamAppID<th>
    <th>Support Info<th>
    <th>Website<th>
    <th>Detailed Description<th>
    <th>Short Description<th>
    <th>Age Requirement</th>
    <th>Platform ("platforms")</tr>
    <th>languages ("supported languages") </th>
    <th>tags ("categories") </th>
  </tr>
</table>
<br><br>
<b>Demo Schema</b>
<table>
  <tr>
    <th>SteamAppID<th>
    <th>Support Info<th>
    <th>Name</th>
    <th>Base_price</th>
    <th>Current_Price</th>
    <th>Developer </th>
    <th>Publisher</th>
    <th>Release_data</th>
    <th>Images</th>
    <th>Website<th>
    <th>Age Requirement<th>
    <th>Detailed Description<th>
    <th>Short Description<th>
    <th>Platform ("platforms")</tr>
    <th>languages ("supported languages") </th>
    <th>tags ("categories") </th>
  </tr>
</table>
- Note: Any thing with a * may be an issue <br>
- Note: Some Schema for Games table I did not see in JSON but were apart of our original idea. Examples include Microtransactions and Franchise.

```
PrimaryKey: SteamAppID
ForeignKey: ?
```
# Project Ideas
- [x] Steam Game Market

# Dependencies
- Django==5.0.1
- beautifulsoup4==4.12.3
- python-steam-api==1.2.2
- mySQL: https://dev.mysql.com/downloads/file/?id=526407 
