from django.urls import path

from . import views

urlpatterns = [
    path("", views.base, name="base"),
    
    path("home/", views.home, name="home" ),
    path("games/", views.games, name="games" ),
    path("DLC/", views.dlc_view, name="DLC"),
    path("music/", views.music, name="music"),
    path("demo/", views.demo, name="demo"),
    path("user/", views.user, name="user"),
]
