from django import forms
from .models import *

class AlarmForm(forms.ModelForm):
    class Meta:
        model = FormPadre
        fields = ['tipoSiniestro','hora','direccion','altura','referencia','nombre','telefono']

class AVform(forms.ModelForm):
    class Meta:
        model = AccidenteVehicular
        fields = '__all__'
        exclude = ['idAlarma']

class IFform(forms.ModelForm):
    class Meta:
        model = IncendioForestal
        fields = '__all__'
        exclude = ['idAlarma']

class IBform(forms.ModelForm):
    class Meta:
        model = IncendioBaldio
        fields = '__all__'
        exclude = ['idAlarma']

class IVform(forms.ModelForm):
    class Meta:
        model = IncendioVivienda
        fields = '__all__'
        exclude = ['idAlarma']

class IVhform(forms.ModelForm):
    class Meta:
        model = IncendioVehicular
        fields = '__all__'
        exclude = ['idAlarma']

class IEform(forms.ModelForm):
    class Meta:
        model = IncendioElectrico
        fields = '__all__'
        exclude = ['idAlarma']

class RAform(forms.ModelForm):
    class Meta:
        model = RescateAnimal
        fields = '__all__'
        exclude = ['idAlarma']

class RCform(forms.ModelForm):
    class Meta:
        model = RescateCadaver
        fields = '__all__'
        exclude = ['idAlarma']