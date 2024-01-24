from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Syntax: for rendering, so inside of these template html files will be a {{}} that uses a dictionary. 
# render(response, htmlFile, dict)
# dictionary will have variable tokens so that way you can put them into the application.
# NOTE: Use this aspect of django to render informationf from the database

def index(response):
    my_dict = dict()
    my_dict["game"] = "Baldur's Gate III"
    return render(response, "main/base.html", my_dict)

def home(response):
    return render(response, "main/home.html", {})
