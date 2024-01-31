from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from auteurs.forms import AuteurForms
from auteurs.models import Auteur

from localization.models import Geolocalization

@login_required
def auteur_statistique(request):
    return render(request, 'auteur_statistiques.html')

@login_required
def auteur_retrieve(request, id):
    auteur = Auteur.objects.get(id=id)
    return render(request, 'auteur_details.html', {"auteur": auteur})

@login_required
def auteur_list(request):
    auteurs = Auteur.objects.all()
    return render(request, 'auteur_lists.html', {"auteurs": auteurs})

@login_required
def auteur_create(request):
    if request.method == "POST":
        auteur_form = AuteurForms(request.POST)
        if auteur_form.is_valid():
            auteur = auteur_form.save()
            if auteur_form.cleaned_data['geolocalisation_latitude'] is not None and auteur_form.cleaned_data['geolocalisation_longitude'] is not None:
                latitude = auteur_form.cleaned_data['geolocalisation_latitude']
                longitude = auteur_form.cleaned_data['geolocalisation_longitude']
                geolocalisation = Geolocalization.objects.create(
                    latitude=latitude,
                    longitude=longitude
                )
                auteur.geolocalisation = geolocalisation
                auteur.save()
            return redirect('auteur-details', auteur.id)
    else:
        auteur_form = AuteurForms()

    return render(request, 'auteurs_create.html', {"auteur_form": auteur_form})

@login_required
def auteur_update(request, id):
    auteur = Auteur.objects.get(id=id)

    if request.method == "POST":
        auteur_form = AuteurForms(request.POST, instance=auteur)

        if auteur_form.is_valid():
            auteur = auteur_form.save()
            latitude = auteur_form.cleaned_data['geolocalisation_latitude']
            longitude = auteur_form.cleaned_data['geolocalisation_longitude']
            geolocalisation = auteur.geolocalisation
            if latitude is not "  " and longitude is not "  " and geolocalisation is not None:
                geo = Geolocalization.objects.get(id=geolocalisation.id)
                geo.delete()

            elif latitude is not None and longitude is not None and geolocalisation is not None:
                geo = Geolocalization.objects.get(id=geolocalisation.id)
                geo.latitude = latitude
                geo.longitude = longitude
                geo.save()
            elif latitude is not None and longitude is not None and geolocalisation is None:
                geo = Geolocalization.objects.create(
                    latitude=latitude,
                    longitude=longitude
                )
                auteur.geolocalisation = geo
                auteur.save()

            return redirect('auteur-details', auteur.id)
    else:
        auteur_form = AuteurForms(instance=auteur)

    return render(request, 'auteur_update.html', {"auteur_form": auteur_form})

@login_required
def auteur_destroy(request, id):
    auteur = Auteur.objects.get(id=id)
    if request.method == "POST":
        auteur.delete()
        return redirect('auteur-list')
    return render(request, 'auteur_delete.html', {"auteur": auteur})


