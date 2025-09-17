from django import forms
from .models import Vuelo , Aerolinea

class VueloForm(forms.ModelForm):
    class Meta:
        model=Vuelo
        fields=['codigo', 'origen', 'destino']

class AerolineaForm(forms.ModelForm):
    class Meta:
        model=Aerolinea
        fields=['nombre', 'pais_origen','vuelo']