from django import forms

from auteurs.models import Auteur


class AuteurForms(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'