from django import forms
from rango.models import Tapas, Bares

class TapasForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduzca el nombre de la tapa")
    votos = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Tapas
        fields = ('nombre','bar',)