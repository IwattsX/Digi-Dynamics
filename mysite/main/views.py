from django.shortcuts import render
from django.http import HttpResponse
from .forms import Games, Demo, DLC, Music
from .models import select

import re

# Create your views here.
# Syntax: for rendering, so inside of these template html files will be a {{}} that uses a dictionary. 
# render(response, htmlFile, dict)
# dictionary will have variable tokens so that way you can put them into the application.
# NOTE: Use this aspect of django to render informationf from the database


def GamesSearchHandler(response, searchBy: str, games : list):

    print(searchBy)
    if searchBy == 'name':
        name = response.GET.get('name', None)
        
        # This doesn't display anything and doesn't do the name REGEXP '' that will always be true
        if name is None or name == "":
            return
        Games_res = select("Games", columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date", 
        whereClause=f"Name REGEXP '{name}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)
    
    elif searchBy == "genre":
        genres = response.GET.getlist('genres', None)

        # Same thing, we want input there
        if genres is None or len(genres) == 0:
            return
        
        genres_regex = ""
        for i, genre in enumerate(genres):
            genres_regex += f"({genre})"
            if i == len(genres) - 1:
                break
            genres_regex += "|"

        # print(genres_regex)

        Games_res = select("Games", columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                           whereClause=f"Genre REGEXP '{genres_regex}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)

    elif searchBy == 'publisher':
        publisher = response.GET.get('name', None)
        if publisher is None or publisher == "":
            return
        
        Games_res = select("Games",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                            whereClause=f"Publisher LIKE '%{publisher}%'")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)

    elif searchBy == 'developer':
        developer = response.GET.get('name', None)
        if developer is None or developer == "":
            return
        Games_res = select("Games",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                        whereClause=f"Developer LIKE '%{developer}%'")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)


    elif searchBy == 'price':
        priceStr = response.GET.get('price', None)
        if priceStr is None or priceStr == "":
            return
        

        price = float(priceStr) * 100


        Games_res = select("Games",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                    whereClause=f"Current_price < {price}")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)


    elif searchBy == 'dateyear':
        date = response.GET.get('year', None)
        if date is None or date == "":
            return
        
        year = int(date)

        Games_res = select("Games",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                    whereClause=f"Release_Date REGEXP '\\\\d{{4}}'")
        
        for row in Games_res:
            regex_year = "(\\d{4})"
            release_str = row["Release_Date"]
            temp = re.search(regex_year, release_str)

            release_year = int(temp.group(1))
            if year == release_year:
                # print(f"Year {year} release_year = {release_year}")
                if not row.get("Base_price") is None:
                    row["Base_price"] = row["Base_price"]/100
                if not row.get("Current_price") is None:
                    row["Current_price"] = row["Current_price"]/100
                games.append(row)
        




def base(response):
    my_dict = dict()
    # my_dict["game"] = ["Baldur's Gate III", "Terraria"]
    return render(response, "main/base.html", my_dict)

def home(response):
    return render(response, "main/home.html", {})

"""
Both are Dictionaries:
Response.POST 
Response.GET
For games, these dictionaries will contain the div 

syntax: response.GET.get(key, default)
"""

def games(response):
    name = ""
    form = Games()
    games = []
    # This if statement will never run bc the response.method will be "GET"
    if response.method == "POST":
        if form.is_valid():
            form = Games(response.POST)
        return render(response, "main/games.html", {})
            
    elif response.method == "GET":
        print("GET REQUEST")
        print(response.GET)

        searchBy = response.GET.get("SearchBy", None)

        print(searchBy)

        GamesSearchHandler(response, searchBy, games) 


    return_dict = {
        "form": form,
        "name" : name,
        "games" : games,
        "display": "none" if len(games) == 0 else "block"
    }

    
    return render(response, "main/games.html", return_dict)


def music(response):
    form = Music()
    Music_list = []
    if response.method == "GET":
        print("Get response for music")
        print(response.GET)
        Song_name = response.GET.get('name', None)

        Games_res = select("Music", columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date", 
        whereClause=f"Name REGEXP '{Song_name}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            Music_list.append(row)
    return_dict = {
        'form' : form,
        "musics" : Music_list,
        "display": "none" if len(Music_list) == 0 else "block"
    }
    return render(response, "main/music.html", return_dict)


def dlc_view(response):
    form = DLC()
    if response.method == "POST":
        form = DLC(response.POST)
        if form.is_valid():
            pass
    else:
        pass
    return render(response, "main/DLC.html", {'form' : form})


def demo(response):
    form = Demo()
    if response.method == "POST":
        form = Demo(response.POST)
        if form.is_valid():
            pass
    else:
        pass
    return render(response, "main/demo.html", {'form' : form})

def user(response):
    return render(response, "main/user.html", {})
