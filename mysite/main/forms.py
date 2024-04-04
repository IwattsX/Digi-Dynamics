from django import forms
from .choices import GameSearch_CHOICES, GENRE_CHOICES


class Games(forms.Form):
    name = forms.CharField(label="", max_length=200, required=False, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter Game Name",
                "id": "placeholderName"
            }
        ),
    )
    year = forms.IntegerField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter year",
                "pattern" : "([0-9]{2})|([0-9]{4})",
                "title" : "Must be either YY or YYYY format",
                "id" : "placeholderYear",
            }
        ),
    )

    price = forms.FloatField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter price",
                "pattern" : "[0-9]*(?:\.[0-9]{2})?",
                "title" : "Input should be x.xx",
                "id" : "placeholderPrice",
            }
        ),
    )

    # The display:none is a way I was trying to do the .hide() .show() earlier, however Jquery solved this
    genres = forms.MultipleChoiceField(label="", choices=GENRE_CHOICES, required=False, 
                                       widget=forms.CheckboxSelectMultiple(
        attrs={
            "id" : "GameGenres",
            # "style": "display:none;",
        }
        ),
    )


    SearchBy = forms.ChoiceField(choices=GameSearch_CHOICES, label="Search by", 
                                    widget=forms.Select(
                                         attrs={
                                            'id': 'searchBy'
                                            }
                                        )
                                )
    #NSFW = forms.BooleanField(required=False, label="NSFW")

class Music(forms.Form):
    name = forms.CharField(label="Song name", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter Soundtrack Name",
            }
        ),
    )

class DLC(forms.Form):
    name = forms.CharField(label="", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter DLC Name",
            }
        ),
    )

class Demo(forms.Form):
    name = forms.CharField(label="", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter Demo Name",
            }
        ),
    )
