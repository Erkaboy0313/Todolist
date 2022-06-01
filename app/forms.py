from django import forms

class CreateList(forms.Form):
    name = forms.CharField(max_length=150)

class Loginform(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)