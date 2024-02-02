from django.contrib.auth.models import AbstractUser
from django.db import models

from pictures.models import Images


class User(AbstractUser):
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICE = (
        (CREATOR, "Créateur"),
        (SUBSCRIBER, "Abonné")
    )

    profile_photo = models.ForeignKey(Images, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICE)
