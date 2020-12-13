from django import forms
from django.forms import widgets


class MusicianForm(forms.Form):
    author = forms.CharField(max_length=100, required=True, label='Author')
    song = forms.CharField(max_length=2000, label='Song', widget=widgets.Textarea)
    position = forms.IntegerField(label='Position', min_value=0, required=True)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=120, required=False)
