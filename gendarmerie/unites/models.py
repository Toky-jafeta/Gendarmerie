from django.db import models

from gendarmerie.localization.models import Faritany, Geolocalization


class Cirgn(models.Model):
    name = models.CharField(max_length=50, unique=True)
    faritany = models.ForeignKey(Faritany, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Groupement(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cirgn = models.ForeignKey(Cirgn, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Compagnie_terr(models.Model):
    name = models.CharField(max_length=50, unique=True)
    groupement = models.ForeignKey(Groupement, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Compagnie_front(models.Model):
    name = models.CharField(max_length=50, unique=True)
    groupement = models.ForeignKey(Groupement, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Centre_S_Aguerissement_O(models.Model):
    name = models.CharField(max_length=50, unique=True)
    groupement = models.ForeignKey(Groupement, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Brigade_terr(models.Model):
    name = models.CharField(max_length=50, unique=True)
    compagnie = models.ForeignKey(Compagnie_terr, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Brigade_aeroport(models.Model):
    name = models.CharField(max_length=50, unique=True)
    compagnie = models.ForeignKey(Compagnie_front, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Brigade_port(models.Model):
    name = models.CharField(max_length=50, unique=True)
    compagnie = models.ForeignKey(Compagnie_front, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Poste_avance(models.Model):
    name = models.CharField(max_length=50, unique=True)
    brigade = models.ForeignKey(Brigade_terr, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)


class Poste_fixe(models.Model):
    name = models.CharField(max_length=50, unique=True)
    brigade = models.ForeignKey(Brigade_terr, on_delete=models.SET_NULL)
    Poste_avance = models.ForeignKey(Poste_avance, on_delete=models.SET_NULL)
    geolocalization = models.ForeignKey(Geolocalization, on_delete=models.SET_NULL)