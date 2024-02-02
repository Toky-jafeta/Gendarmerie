from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

from auteurs.forms import AuteurForms
from auteurs.models import Auteur

from localization.models import Geolocalization
from localization.forms import GeolocalizationForms
from pictures.forms import ImageForm


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
    auteur_form = AuteurForms()
    geolocalisation_form = GeolocalizationForms()
    upload_image_form_set = formset_factory(ImageForm, extra=5)
    upload_image_forms = upload_image_form_set()
    if request.method == "POST":
        auteur_form = AuteurForms(request.POST)
        geolocalisation_form = GeolocalizationForms(request.POST)
        if auteur_form.is_valid():
            auteur = auteur_form.save(commit=False)

            if geolocalisation_form.is_valid():
                geolocalisation = geolocalisation_form.save()
                auteur.geolocalisation = geolocalisation

            for form in upload_image_forms:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()

            auteur.save()
            return redirect('auteur-details', auteur.id)

    return render(request, 'auteurs_create.html', {"auteur_form": auteur_form, "geolocalisation_form": geolocalisation_form, "upload_image_forms": upload_image_forms})

@login_required
def auteur_update(request, id):
    auteur = Auteur.objects.get(id=id)
    auteur_form = AuteurForms(instance=auteur)
    geolocalisation, geolocalisation_form = None, None
    if auteur.geolocalisation:
        geolocalisation = Geolocalization.objects.get(id=auteur.geolocalisation.id)
        geolocalisation_form = GeolocalizationForms(instance=geolocalisation)

    if request.method == "POST":
        auteur_form = AuteurForms(request.POST, instance=auteur)
        geolocalisation_form = GeolocalizationForms(request.POST, instance=geolocalisation)
        if auteur_form.is_valid():
            auteur = auteur_form.save(commit=False)
            if geolocalisation_form.is_valid():
                geolocalisation = geolocalisation_form.save()
                auteur.geolocalisation = geolocalisation

            auteur.save()

            return redirect('auteur-details', auteur.id)

    return render(request, 'auteur_update.html', {"auteur_form": auteur_form, "geolocalisation_form": geolocalisation_form})

@login_required
def auteur_destroy(request, id):
    auteur = Auteur.objects.get(id=id)
    if request.method == "POST":
        auteur.delete()
        return redirect('auteur-list')
    return render(request, 'auteur_delete.html', {"auteur": auteur})


