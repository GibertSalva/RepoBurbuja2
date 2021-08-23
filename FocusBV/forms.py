from django import forms
from .models import *

class AlarmForm(forms.ModelForm):
    class Meta:
        model = FormPadre
        fields = '__all__'
        exclude = ['idAlarma']

class AVform(forms.ModelForm):
    class Meta:
        model = AccidenteVehicular
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TimeInput(attrs={'class': 'form-control fs-5','id':'reloj'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id':'floatingTextarea2', 'style':'height: 150px'})),
            'claseAC': forms.RadioSelect(attrs={'class': ''}),
            'cantVehiculos': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantPersonas': forms.NumberInput(attrs={'class': 'form-control'}),
            'corteTransito': forms.CheckboxInput(attrs={'class':'form-check-inline'}),
            'tipoCalle':forms.RadioSelect(),
            'servEmergencia': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'herido': forms.TextInput(attrs={'class': 'form-control'}),

        }

class IFform(forms.ModelForm):
    class Meta:
        model = IncendioForestal
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TextInput(attrs={'class': 'form-control shadow'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'sentido': forms.TextInput(attrs= ({'class': 'form-control fs-5'})),
            'riesgoProp': forms.RadioSelect(choices=[(True, 'SI'),(False, 'NO')],attrs= ({'class': 'checkbox-inline'})),
            'edificios': forms.NumberInput(attrs= ({'class': 'form-control fs-5', 'min': 0})),
            'servEmergencia': forms.TextInput(attrs = ({'class': 'form-control fs-5'})),

        }

class IBform(forms.ModelForm):
    class Meta:
        model = IncendioBaldio
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TextInput(attrs={'class': 'form-control shadow'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
        }

class IVform(forms.ModelForm):
    class Meta:
        model = IncendioVivienda
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TextInput(attrs={'class': 'form-control shadow'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
        }

class IVhform(forms.ModelForm):
    class Meta:
        model = IncendioVehicular
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TextInput(attrs={'class': 'form-control shadow'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
        }

class IEform(forms.ModelForm):
    class Meta:
        model = IncendioElectrico
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TextInput(attrs={'class': 'form-control shadow'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
        }

class RAform(forms.ModelForm):
    class Meta:
        model = RescateAnimal
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
        }

class RCform(forms.ModelForm):
    class Meta:
        model = RescateCadaver
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TextInput(attrs={'class': 'form-control shadow'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
        }