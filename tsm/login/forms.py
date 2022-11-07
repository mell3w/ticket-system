from django import forms
from .models import AdvUser

class AdvUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password'}))

