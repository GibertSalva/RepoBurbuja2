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
            'hora': forms.TextInput(attrs={'class': 'form-control shadow'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id':'floatingTextarea2', 'style':'height: 150px'})),
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
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
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
            'hora': forms.TextInput(attrs={'class': 'form-control shadow'}),
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