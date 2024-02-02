from django import forms

from pictures.models import Images


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image', 'caption']
