from django.db import models

# Create your models here.

# Use this to model everything in the databases
# NOTE: May not use django.db since we are using mySQL instead with mysql-connector
class Games_Model():
    def __init__(self, id, name, short_desc) -> None:
        self.id : str = id
        self.name : str = name
        self.short_desc : str = short_desc
        pass
    


# Example here
# class Games(models.Model):
#     steamAppID = models.IntegerField