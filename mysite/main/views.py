from django.shortcuts import render
from django.http import HttpResponse
from .forms import Games, Demo, DLC, Music

# Create your views here.
# Syntax: for rendering, so inside of these template html files will be a {{}} that uses a dictionary. 
# render(response, htmlFile, dict)
# dictionary will have variable tokens so that way you can put them into the application.
# NOTE: Use this aspect of django to render informationf from the database

def base(response):
    my_dict = dict()
    my_dict["game"] = ["Baldur's Gate III", "Terraria"]
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
    nsfw = "NO"
    form = Games()
    if response.method == "POST":
        if form.is_valid():
            form = Games(response.POST)
        return render(response, "main/games.html", {})
            
    else:
        print("GET REQUEST")
        print(response.GET)
        name = response.GET.get('name', 'No NAME')
        if response.GET.get('NSFW'):
            nsfw = response.GET['NSFW']

    return_dict = {
        "form": form,
        "name" : name,
        "NSFW" : "no" if nsfw == 'NO' else "YES",
    }

    
    return render(response, "main/games.html", return_dict)


def music(response):
    form = Music()
    if response.method == "POST":
        form = Music(response.POST)
        if form.is_valid():
            pass
    else:
        pass
    return render(response, "main/music.html", {'form' : form})


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
