from django.db import models

# Create your models here.

class Pokedex(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    numero = models.IntegerField()
    adresse_email = models.EmailField()
    
    def __str__(self):
        return f'{self.nom}'