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
<<<<<<< Updated upstream
                                            'id': 'searchByMusic'
=======
<<<<<<< HEAD
                                            "class" : 'searchBy',
=======
                                            'id': 'searchByMusic'
>>>>>>> c7f5f83203db794b03223e3335c0cd65ca11cae8
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                                            'id': 'searchByDLC'
=======
<<<<<<< HEAD
                                            "class" : 'searchBy',
=======
                                            'id': 'searchByDLC'
>>>>>>> c7f5f83203db794b03223e3335c0cd65ca11cae8
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            "id" : "Game Genres",
=======
<<<<<<< HEAD
            "class" : "Genres",
=======
            "id" : "Game Genres",
>>>>>>> c7f5f83203db794b03223e3335c0cd65ca11cae8
>>>>>>> Stashed changes
            # "style": "display:none;",
        }
        ),
    )


    SearchBy = forms.ChoiceField(choices=GameSearch_CHOICES, label="Search by", 
                                    widget=forms.Select(
                                         attrs={
<<<<<<< Updated upstream
                                            'id': 'searchByDemo'
=======
<<<<<<< HEAD
                                            "class" : 'searchBy',
=======
                                            'id': 'searchByDemo'
>>>>>>> c7f5f83203db794b03223e3335c0cd65ca11cae8
>>>>>>> Stashed changes
                                            }
                                        )
                                )
