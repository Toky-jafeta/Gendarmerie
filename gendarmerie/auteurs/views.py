from django.shortcuts import render

from auteurs.forms import AuteurForms


def auteur_create(request):
    auteur_form = AuteurForms()
    return render(request, 'auteurs_create.html', {"auteur_form": auteur_form})
