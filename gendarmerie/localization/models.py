from django.db import models


class Geolocalization(models.Model):
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)


class Faritany(models.Model):
    name = models.CharField(max_length=20, unique=True)


class District(models.Model):
    name = models.CharField(max_length=20, unique=True)
    faritany = models.ForeignKey(Faritany, on_delete=models.SET_NULL, null=True)


class Commune(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)


class Fokontany(models.Model):
    name = models.CharField(max_length=50)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True)


class Secteur(models.Model):
    name = models.CharField(max_length=50)
    fokontany = models.ForeignKey(Fokontany, on_delete=models.SET_NULL, null=True)
