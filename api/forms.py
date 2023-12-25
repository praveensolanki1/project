from django import forms


class Newform(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(max_value=200)