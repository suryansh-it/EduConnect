from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm): #A built-in Django form for user creation. 
                                                #It includes built-in validation for password fields (password1,password2).
    class Meta:                                 #The Meta class provides metadata about the form.
        model = User
        fields = ["username" , "email" , "password1" , "password2"]