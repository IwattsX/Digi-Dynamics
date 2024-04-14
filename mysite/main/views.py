from django.shortcuts import render
from django.http import HttpResponse
from .forms import Games, Demo, DLC, Music, userform
from .models import select
from .ReadGames.database.generate_pass import gen_pass
from .ReadGames.database.Connect_DB import connect


from .Search_handlers import searchHander

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

        searchHander(response,"Games", searchBy, games) 


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
        searchBy = response.GET.get("SearchBy", None)
        searchHander(response, "Music", searchBy, Music_list)
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
        searchHander(response, "DLC", searchBy, DLC_list)
    
    return_dict = {
        'form' : form,
        'DLC' : DLC_list,
        "display": "none" if len(DLC_list) == 0 else "block"
    }

    return render(response, "main/DLC.html", return_dict)


def demo(response):
    form = Demo()
    if response.method == "GET":
        pass
    return render(response, "main/demo.html", {'form' : form})

def user_Handler(username, password):
    res = False
    cnx = connect()
    cursor = cnx.cursor(dictionary=True)

    query = "SELECT * FROM user WHERE username = %s AND pass = %s"
    generated_pass = gen_pass(password)
    if not generated_pass is None: 
        cursor.execute(query, (username, generated_pass[0]))
        res = cursor.fetchone()
    if res:
        return True
    else:
        return False



def user(response):
    form = userform(response.POST or None)
    login_msg = None
    if response.method == "POST" and form.is_valid():
        uname = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        if user_Handler(uname, password):
            login_msg = "Login successful"
        else:
            login_msg = "Login error"

    return_dict = {
        "form" : form,
        "alert_msg": login_msg
    }
    return render(response, "main/history.html", return_dict)
