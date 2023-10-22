from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label="SearchBar", max_length=300)