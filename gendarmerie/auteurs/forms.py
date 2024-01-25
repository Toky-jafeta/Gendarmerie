from django import forms
from django.forms import SelectDateWidget
from django.forms.models import inlineformset_factory

from auteurs.models import Auteur

from localization.forms import GeolocalizationForms


class AuteurForms(forms.ModelForm):

    class Meta:
        model = Auteur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AuteurForms, self).__init__(*args, **kwargs)

        self.fields['secteur'].required = False
        self.fields['fokontany'].required = False
        self.fields['geolocalisation'].required = False

        self.fields['birthday'].widget = SelectDateWidget(
            empty_label=("Année", "Mois", "Jour")
        )

        self.fields['geolocalisation'].widget = forms.HiddenInput()

        for field_name, field in GeolocalizationForms().fields.items():
            self.fields['geolocalisation_' + field_name] = field
            self.fields['geolocalisation_' + field_name].required = False
