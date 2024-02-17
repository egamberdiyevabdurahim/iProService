from django import forms

from .models import *


class UserForm(forms.Model):
    class Meta:
        model = User
        fields = ['username', 'password', 'photo']