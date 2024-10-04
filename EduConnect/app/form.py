from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:                             #The Meta class provides metadata about the form.
        model = User
        fields = ["username" , "email" , "password1" , "password2"]