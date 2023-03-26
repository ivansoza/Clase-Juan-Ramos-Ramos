from django import forms
from .models import Placa

class PlacaForm(forms.ModelForm):
    class Meta:
        model = Placa
        fields = '__all__'
