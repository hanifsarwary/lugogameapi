from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','password']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields