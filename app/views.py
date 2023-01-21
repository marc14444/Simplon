from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import PokedexForm
from . import models
from .models import Pokedex
from django import forms
# Create your views here.


def home(request):
    submited = False
    if request.method == "POST":
        form = PokedexForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/recup', {'form':form})
    else:
        form = PokedexForm
        if 'submited' in request.GET:
            submited = True
    return render(request, "app/index.html", {'form':form})


def recup(request):
    donnee = Pokedex.objects.all()
    return render(request, 'app/recup.html', {'donnee':donnee})