from django import forms
from django.forms import fields
import datetime
from .models import *

class dateForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today,required=False)

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
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(attrs=({'class': 'form-control', 'id':'floatingTextarea2', 'style':'height: 150px'})),
            'claseAC': forms.RadioSelect(attrs={'class': ''}),
            'cantVehiculos': forms.Textarea(attrs=({'class': 'form-control fs-5', 'id': 'mytextarea', 'style':'height: 150px'})),
            'cantPersonas': forms.NumberInput(attrs={'class': 'form-control'}),
            'corteTransito': forms.RadioSelect(choices=[(True, 'SI'),(False, 'NO')],attrs= ({'class': 'checkbox-inline'})),
            'tipoCalle':forms.RadioSelect(),
            'servEmergencia': forms.TextInput(attrs={'class': 'form-control fs-6'}),
            'herido': forms.TextInput(attrs={'class': 'form-control'}),
        }


class IFform(forms.ModelForm): #HECHO
    class Meta:
        model = IncendioForestal
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
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
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'entreCalles': forms.TextInput(attrs={'class':'form-control fs-5'}),
            'riesgoProp': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')],
                                            attrs=({'class': 'checkbox-inline fs-5', 'style' : 'width: 10%' 'height: 2em'})),
        }

class IVform(forms.ModelForm): #HECHO
    class Meta:
        model = IncendioVivienda
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
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
            'espera': forms.RadioSelect(choices=[(True, 'SI'),(False, 'NO')],attrs= ({'class': 'checkbox-inline', 'style' : 'width: 10%' 'height: 2em'})),

        }

class IVhform(forms.ModelForm):#Hecho
    class Meta:
        model = IncendioVehicular
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'tipoVehiculo': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'humoLlamas': forms.Textarea(attrs={'class': 'form-control fs-5', 'style': 'height: 150px'}),
            'vehiculoOcup': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')],
                                            attrs=({'class': 'checkbox-inline'})),
            'gnc':forms.Textarea(attrs={'class': 'form-control shadow','style': 'height: 100px'}),
            'riesgoProp': forms.RadioSelect(choices=[(True, 'SI'), (False, 'NO')],
                                           attrs=({'class': 'checkbox-inline'})),
        }

class IEform(forms.ModelForm): #HECHO
    class Meta:
        model = IncendioElectrico
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
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
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'animal': forms.TimeInput(attrs={'class': 'form-control shadow'}),    
            'condicionAnimal': forms.TimeInput(attrs={'class': 'form-control shadow', 'style': 'height: 100px'}),
            'vision': forms.RadioSelect(choices=[(True, 'SI'),(False, 'NO')],attrs= ({'class': 'checkbox-inline'})),
        }

class RCform(forms.ModelForm): #HECHO
    class Meta:
        model = RescateCadaver
        fields = '__all__'
        exclude = ['idAlarma']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
        }

class AUXform(forms.ModelForm): #HECHO
    class Meta:
        model = FormularioAuxiliar
        fields = '__all__'
        
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'aux': forms.Textarea(attrs=({'class': 'form-control', 'id': 'mytextarea', 'style':'height: 150px'})),
        }

class EGform(forms.ModelForm):
    class Meta:
        model = EscapeGas
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'tipoIncidente': forms.Textarea(attrs=({'class': 'form-control', 'style':'height: 150px'})),
        }

class RPVform(forms.ModelForm):
    class Meta:
        model = RescatePersonaVia
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'estadoPersona': forms.Textarea(attrs=({'class': 'form-control', 'style':'height: 150px'})),
            'lesion': forms.Textarea(attrs={'class':'form-contol fs-5', 'style':'height: 150px'})           
        }

class PCform(forms.ModelForm):
    class Meta:
        model = PerdidaCombustible
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control shadow','readonly': True}),
            'hora': forms.TimeInput(attrs={'class': 'form-control shadow','id':'reloj','readonly': True}),
            'receptor': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'referencia': forms.Textarea(
                attrs=({'class': 'form-control', 'id': 'floatingTextarea2', 'style': 'height: 150px'})),
            'tipoCombustible': forms.TextInput(attrs=({'class': 'form-control'})),
            'servEmergencia': forms.Textarea(attrs={'class':'form-contol fs-5', 'style':'height: 150px'}),
            'hayVictimas': forms.TextInput(attrs=({'class':'form-control fs-5'}))           
        }
