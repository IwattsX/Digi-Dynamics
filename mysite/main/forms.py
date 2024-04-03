from django import forms

class Games(forms.Form):
    name = forms.CharField(label="", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter Game Name",
                "id": "placeholderName"
            }
        ),
    )
    # choices.py
    GameSearch_CHOICES = (
        ('name', 'Name'),
        ('genre', 'Genre'),
        ('publisher', 'Publisher'),
        ('developer', 'Developer'),
        ('price', 'Price'),
        ('dateyear', 'Date (Year)'),
    )

    SearchBy = forms.ChoiceField(choices=GameSearch_CHOICES, label="Search by")
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
