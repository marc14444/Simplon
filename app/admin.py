from django.contrib import admin
from app.models import *
# Register your models here.

class PokedexAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'numero', 'adresse_email')


admin.site.register(Pokedex, PokedexAdmin)