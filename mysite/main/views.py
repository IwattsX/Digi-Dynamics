from django.shortcuts import render
from django.http import HttpResponse
from .forms import Games, Demo, DLC, Music
from .models import select


from .Search_handlers import GamesSearch_Handler, DLCSearch_Handler

# Create your views here.
# Syntax: for rendering, so inside of these template html files will be a {{}} that uses a dictionary. 
# render(response, htmlFile, dict)
# dictionary will have variable tokens so that way you can put them into the application.
# NOTE: Use this aspect of django to render informationf from the database



        




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

        GamesSearch_Handler(response, searchBy, games) 


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
    DLC_list = []
    if response.method == "GET":
        searchBy = response.GET.get("SearchBy", None)

        # print(searchBy)
        DLCSearch_Handler(response, searchBy, DLC_list)
    
    return_dict = {
        'form' : form,
        'DLC' : DLC_list,
        "display": "none" if len(DLC_list) == 0 else "block"
    }

    return render(response, "main/DLC.html", return_dict)


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
