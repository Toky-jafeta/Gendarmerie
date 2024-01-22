from django.db import models


class Auteur(models.Model):
    """a voir pour le fokontany, commune, district, ..."""
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    Address = models.CharField(max_length=255)
    comment = models.TextField(blank=True)


