from django.db import models

from localization.models import Fokontany, Secteur


class Auteur(models.Model):
    """a voir pour le fokontany, commune, district, ..."""
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    Address = models.CharField(max_length=255) #Adresse, lot trano na raha tsy misy lot trano dia localisé-na amin'ny alalan'ny fanazavana ilay toerana
    secteur = models.ForeignKey(Secteur, on_delete=models.SET_NULL, null=True) #secteur misy an'ilay fokontany
    fokontany = models.ForeignKey(Fokontany, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True)