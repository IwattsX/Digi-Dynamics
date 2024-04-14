from django import forms
from .choices import GameSearch_CHOICES, GENRE_CHOICES, MusicSearch_CHOICES, DemoSearch_CHOICES, DlcSearch_CHOICES


class Games(forms.Form):
    name = forms.CharField(label="", max_length=200, required=False, widget=forms.TextInput(
            attrs={
                "class": "nameSearch",
                "placeholder": "Enter Game Name",
            }
        ),
    )
    year = forms.IntegerField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "yearSearch",
                "placeholder": "Enter year",
                "pattern" : "([0-9]{4})",
                "title" : "Must be in YYYY format",
            }
        ),
    )

    price = forms.FloatField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "priceSearch",
                "placeholder": "Enter price",
                "pattern" : "[0-9]*(?:\\.[0-9]{2})?",
                "title" : "Input should be x.xx",
            }
        ),
    )

    # The display:none is a way I was trying to do the .hide() .show() earlier, however Jquery solved this
    genres = forms.MultipleChoiceField(label="", choices=GENRE_CHOICES, required=False, 
                                       widget=forms.CheckboxSelectMultiple(
        attrs={
            "class" : "Genres",
            # "style": "display:none;",
        }
        ),
    )


    SearchBy = forms.ChoiceField(choices=GameSearch_CHOICES, label="Search by", 
                                    widget=forms.Select(
                                         attrs={
                                            "class" : 'searchBy',
                                            }
                                        )
                                )
    #NSFW = forms.BooleanField(required=False, label="NSFW")

class Music(forms.Form):

    name = forms.CharField(label="", max_length=200, required=False, widget=forms.TextInput(
            attrs={
                "class": "nameSearch",
                "placeholder": "Enter Soundtrack Name",
            }
        ),
    )
    year = forms.IntegerField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "yearSearch",
                "placeholder": "Enter year",
                "pattern" : "([0-9]{4})",
                "title" : "Must be in YYYY format",
            }
        ),
    )

    price = forms.FloatField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "priceSearch",
                "placeholder": "Enter price",
                "pattern" : "[0-9]*(?:\\.[0-9]{2})?",
                "title" : "Input should be x.xx",
            }
        ),
    )

    SearchBy = forms.ChoiceField(choices=MusicSearch_CHOICES, label="Search by", 
                                    widget=forms.Select(
                                         attrs={
                                            "class" : 'searchBy',
                                            }
                                        )
                                )

class DLC(forms.Form):
    name = forms.CharField(label="", max_length=200, required=False, widget=forms.TextInput(
            attrs={
                "class": "nameSearch",
                "placeholder": "Enter Game Name",
            }
        ),
    )
    year = forms.IntegerField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "yearSearch",
                "placeholder": "Enter year",
                "pattern" : "([0-9]{4})",
                "title" : "Must be in YYYY format",
            }
        ),
    )

    price = forms.FloatField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "priceSearch",
                "placeholder": "Enter price",
                "pattern" : "[0-9]*(?:\\.[0-9]{2})?",
                "title" : "Input should be x.xx",
            }
        ),
    )

    # The display:none is a way I was trying to do the .hide() .show() earlier, however Jquery solved this
    genres = forms.MultipleChoiceField(label="", choices=GENRE_CHOICES, required=False, 
                                       widget=forms.CheckboxSelectMultiple(
        attrs={
            "class" : "Genres",
            # "style": "display:none;",
        }
        ),
    )


    SearchBy = forms.ChoiceField(choices=GameSearch_CHOICES, label="Search by", 
                                    widget=forms.Select(
                                         attrs={
                                            "class" : 'searchBy',
                                            }
                                        )
                                )
    

class Demo(forms.Form):
    name = forms.CharField(label="", max_length=200, required=False, widget=forms.TextInput(
            attrs={
                "class": "nameSearch",
                "placeholder": "Enter Game Name",
            }
        ),
    )
    year = forms.IntegerField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "yearSearch",
                "placeholder": "Enter year",
                "pattern" : "([0-9]{4})",
                "title" : "Must be in YYYY format",
            }
        ),
    )

    price = forms.FloatField(label="", required=False, widget=forms.TextInput(
            attrs={
                "class": "priceSearch",
                "placeholder": "Enter price",
                "pattern" : "[0-9]*(?:\\.[0-9]{2})?",
                "title" : "Input should be x.xx",
            }
        ),
    )

    # The display:none is a way I was trying to do the .hide() .show() earlier, however Jquery solved this
    genres = forms.MultipleChoiceField(label="", choices=GENRE_CHOICES, required=False, 
                                       widget=forms.CheckboxSelectMultiple(
        attrs={
            "class" : "Genres",
            # "style": "display:none;",
        }
        ),
    )


    SearchBy = forms.ChoiceField(choices=GameSearch_CHOICES, label="Search by", 
                                    widget=forms.Select(
                                         attrs={
                                            "class" : 'searchBy',
                                            }
                                        )
                                )

class user_class(forms.Form):
    username = forms.CharField(max_length=200, required=True, 
                               widget=forms.TextInput(
                                   attrs={
                                       "id" : "username",
                                   },
                               )
                               )
    password = forms.CharField(max_length=200, required=True, 
                               widget=forms.TextInput(
                                   attrs={
                                       "id" : "pass",
                                   },
                               ))