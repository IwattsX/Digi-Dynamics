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
3) Run django
  ```
  python manage.py runserver
  ```
4) Put this URL into the page:
  <a href = "http://127.0.0.1:8000/"><br>http://127.0.0.1:8000/</a>

# TODO
- [ ] Apply steam web API with a database
- [ ] Figure out the schema of steam game market
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
<b>Schema</b>
<table>
  <tr>
    <th>Name</th>
    <th>DLC</th>
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
    <th>Images</th>
    <th>Trailers</th>
    <th> *Platform</tr>
    <th> *languages </th>
    <th> *tags </th>
  </tr>
</table>
- Note: Any thing with a * may be an issue

```
PrimaryKey: ?
CompositeKey: ?
ForeignKey: ?
```
# Project Ideas
- [x] Steam Game Market
