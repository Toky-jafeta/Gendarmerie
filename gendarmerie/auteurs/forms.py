from django import forms
from django.forms import SelectDateWidget
from django.forms.models import inlineformset_factory

from auteurs.models import Auteur


class AuteurForms(forms.ModelForm):

    class Meta:
        model = Auteur
        exclude = ('geolocalisation',)

    def __init__(self, *args, **kwargs):
        super(AuteurForms, self).__init__(*args, **kwargs)

        self.fields['secteur'].required = False
        self.fields['fokontany'].required = False

        self.fields['birthday'].widget = SelectDateWidget(
            empty_label=("Année", "Mois", "Jour")
        )