from django.forms import ModelForm
from django import forms
from .models import Main
from . import models


class RegistrarMain(ModelForm):
    class Meta:
        model = models.Main
        exclude = []
        widgets = {
            'origen': forms.Select(attrs={'class': 'form-control'})}
