from django import forms

from localization.models import Geolocalization


class GeolocalizationForms(forms.ModelForm):
    class Meta:
        model = Geolocalization
        fields = '__all__'