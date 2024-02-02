from django import forms

from localization.models import Geolocalization


class GeolocalizationForms(forms.ModelForm):
    class Meta:
        model = Geolocalization
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GeolocalizationForms, self).__init__(*args, **kwargs)

        self.fields['latitude'].required = False
        self.fields['longitude'].required = False