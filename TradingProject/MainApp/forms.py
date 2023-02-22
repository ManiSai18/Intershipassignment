from django import forms

class uploadform(forms.Form):
    csv_file = forms.FileField()
    time = forms.IntegerField()