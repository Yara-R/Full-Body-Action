from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
