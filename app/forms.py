from django import forms

class CreateList(forms.Form):
    name = forms.CharField(max_length=150)