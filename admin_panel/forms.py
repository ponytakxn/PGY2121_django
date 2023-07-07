from django import forms
from bacca.models import Imagen


class UploadForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ["url_imagen"]
