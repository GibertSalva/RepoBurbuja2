from django import forms
from django.forms import fields
import datetime
from .models import *
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class dateForm(forms.Form):
    date = forms.DateField(required=False, widget=DateInput(),)


class AlarmForm(forms.ModelForm):
    class Meta:
        model = FormPadre
        fields = '__all__'
        exclude = ['idAlarma']
        

# Hecho
class AVform(forms.ModelForm):
    class Meta:
        model = AccidenteVehicular
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style':'height: 150px'})),
            'claseAC': forms.RadioSelect(attrs={'class': ''}),
            'cantVehiculos': forms.Textarea(attrs=({'class': 'form-control fs-5', 'id': 'mytextarea', 'style':'height: 150px'})),
            'cantPersonas': forms.NumberInput(attrs={'class': 'form-control'}),
            'corteTransito': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')], attrs=({'class': 'checkbox-inline'})),
            'tipoCalle':forms.RadioSelect(),
            'servEmergencia': forms.TextInput(attrs={'class': 'form-control fs-6', "autocomplete": "off"}),
            'herido': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
        }


# Hecho
class IFform(forms.ModelForm):
    class Meta:
        model = IncendioForestal
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px', "autocomplete": "off"})),
            'sentido': forms.TextInput(attrs=({'class': 'form-control fs-5', "autocomplete": "off"})),
            'riesgoProp': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')], attrs=({'class': 'checkbox-inline'})),
            'edificios': forms.NumberInput(attrs=({'class': 'form-control fs-5', 'min': 0})),
            'servEmergencia': forms.TextInput(attrs=({'class': 'form-control fs-5', "autocomplete": "off"})),

        }


# Hecho
class IBform(forms.ModelForm):
    class Meta:
        model = IncendioBaldio
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'entreCalles': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'riesgoProp': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')], attrs=({'class': 'checkbox-inline fs-5', 'style' : 'width: 10%' 'height: 2em'})),
        }


# Hecho
class IVform(forms.ModelForm):
    class Meta:
        model = IncendioVivienda
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id':'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'entreCalles': forms.TextInput(attrs=({'class': 'form-control fs-5', "autocomplete": "off"})),
            'estadoFuego': forms.TextInput(attrs=({'class': 'form-control fs-5', "autocomplete": "off"})),
            'habitantes': forms.TextInput(attrs=({'class': 'form-control fs-5', "autocomplete": "off"})),
            'localHabit': forms.TextInput(attrs=({'class': 'form-control fs-5', "autocomplete": "off"})),
            'descVivienda': forms.TextInput(attrs=({'class': 'form-control fs-5', 'style': 'width: 150px', "autocomplete": "off"})),
            'espera': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')], attrs=({'class': 'checkbox-inline', 'style' : 'width: 10%' 'height: 2em'})),

        }


# Hecho
class IVhform(forms.ModelForm):
    class Meta:
        model = IncendioVehicular
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'tipoVehiculo': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'humoLlamas': forms.Textarea(attrs={'class': 'form-control fs-5', 'style': 'height: 150px'}),
            'vehiculoOcup': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')], attrs=({'class': 'checkbox-inline'})),
            'gnc': forms.Textarea(attrs={'class': 'form-control ', 'style': 'height: 100px'}),
            'riesgoProp': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')], attrs=({'class': 'checkbox-inline'})),
        }


# Hecho
class IEform(forms.ModelForm):
    class Meta:
        model = IncendioElectrico
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'desperfecto': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'humoLlamas': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'epec': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'servEmergencia': forms.TextInput(attrs=({'class': 'form-control fs-5', "autocomplete": "off"})),
        }


class RAform(forms.ModelForm):
    class Meta:
        model = RescateAnimal
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5', "autocomplete": "off"}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'animal': forms.TimeInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'condicionAnimal': forms.TimeInput(attrs={'class': 'form-control', 'style': 'height: 100px', "autocomplete": "off"}),
            'vision': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')], attrs=({'class': 'checkbox-inline'})),
        }


# Hecho
class RCform(forms.ModelForm):
    class Meta:
        model = RescateCadaver
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
        }


# HECHO
class AUXform(forms.ModelForm):

    class Meta:
        model = FormularioAuxiliar
        fields = '__all__'
        exclude = ['referencia', ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'auxiliar': forms.Textarea(attrs=({'class': 'form-control fs-5', 'id': 'mytextarea', 'style':'height: 150px'})),
        }


class EGform(forms.ModelForm):
    class Meta:
        model = EscapeGas
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'tipoIncidente': forms.Textarea(attrs=({'class': 'form-control', 'style': 'height: 150px'})),
        }


class RPVform(forms.ModelForm):
    class Meta:
        model = RescatePersonaVia
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'estadoPersona': forms.Textarea(attrs=({'class': 'form-control', 'style': 'height: 150px'})),
            'lesion': forms.Textarea(attrs={'class': 'form-contol fs-5', 'style': 'height: 150px'})
        }


class PCform(forms.ModelForm):
    class Meta:
        model = PerdidaCombustible
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control ', 'readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'reloj', 'readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'tipoCombustible': forms.TextInput(attrs=({'class': 'form-control'})),
            'servEmergencia': forms.Textarea(attrs={'class': 'form-contol fs-5', 'style': 'height: 150px'}),
            'hayVictimas': forms.TextInput(attrs=({'class': 'form-control fs-5'}))
        }
