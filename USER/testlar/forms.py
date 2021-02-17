from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User




class UserC(forms.ModelForm):
    username=forms.CharField(help_text=False)

    class Meta:
        model=User
        fields=('email','password')
