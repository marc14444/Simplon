from django.forms import ModelForm
from . import models
from .models import Pokedex
from django import forms


class PokedexForm(ModelForm):
    class Meta:
        model = Pokedex
        fields = ("nom", "prenom", "numero", "adresse_email")