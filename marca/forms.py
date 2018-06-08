from django.forms import ModelForm
from django import forms
from .models import Marca
from . import models


class RegistrarMarca(ModelForm):
    class Meta:
        model = models.Marca
        exclude = []
