from django import forms
from .models import *

class AlarmForm(forms.ModelForm):
    class Meta:
        model = FormPadre
        fields = '__all__'
        exclude = ['idAlarma']

class AVform(forms.ModelForm): #HECHO
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
            'corteTransito': forms.RadioSelect(choices=[(True, 'SI'),(False, 'NO')],attrs= ({'class': 'checkbox-inline'})),
            'tipoCalle':forms.RadioSelect(),
            'servEmergencia': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'herido': forms.TextInput(attrs={'class': 'form-control'}),

        }

class IFform(forms.ModelForm): #HECHO
    class Meta:
        model = IncendioForestal
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow', 'id': 'reloj'}),
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

class IBform(forms.ModelForm): #HECHO
    class Meta:
        model = IncendioBaldio
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow', 'id': 'reloj'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'entreCalles': forms.TextInput(attrs={'class':'form-control fs-5'}),
            'riesgoProp': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')],
                                            attrs=({'class': 'checkbox-inline'})),
        }

class IVform(forms.ModelForm): #HECHO
    class Meta:
        model = IncendioVivienda
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow', 'id': 'reloj'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'entreCalles': forms.TextInput(attrs= ({'class': 'form-control fs-5'})),
            'estadoFuego': forms.TextInput(attrs= ({'class': 'form-control fs-5'})),
            'habitantes': forms.TextInput(attrs= ({'class': 'form-control fs-5'})),
            'localHabit': forms.TextInput(attrs= ({'class': 'form-control fs-5'})),
            'descVivienda': forms.TextInput(attrs= ({'class': 'form-control fs-5', 'style': 'width: 150px'})),
            'espera': forms.RadioSelect(choices=[(True, 'SI'),(False, 'NO')],attrs= ({'class': 'checkbox-inline'})),

        }

class IVhform(forms.ModelForm):#Hecho
    class Meta:
        model = IncendioVehicular
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow', 'id': 'reloj'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'tipoVehiculo': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'humoLlamas': forms.TextArea(attrs={'class': 'form-control fs-5', 'style': 'height: 150px'}),
            'vehiculoOcup': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')],
                                            attrs=({'class': 'checkbox-inline'})),
            'gnc':forms.TextArea(attrs={'class': 'form-control shadow','style': 'height: 100px'}),
            'riesgoProp': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')],
                                           attrs=({'class': 'checkbox-inline'})),
        }

class IEform(forms.ModelForm): #HECHO
    class Meta:
        model = IncendioElectrico
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow', 'id': 'reloj'}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'desperfecto': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'humoLlamas': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'epec': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'servEmergencia': forms.TextInput(attrs = ({'class': 'form-control fs-5'})),


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