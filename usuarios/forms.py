from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from . import models


class RegisterUser(ModelForm):
    class Meta:
        exclude = []
