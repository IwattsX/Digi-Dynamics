from django import forms

class Games(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    NSFW = forms.BooleanField(required=False, label="NSFW")

class Music(forms.Form):
    name = forms.CharField(label="Song name", max_length=200)

class DLC(forms.Form):
    name = forms.CharField(label="DLC name", max_length=200)

class Demo(forms.Form):
    name = forms.CharField(label="Demo name", max_length=200)
