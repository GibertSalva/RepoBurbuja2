from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField
from django.forms import ModelForm


# Create your models here.
#TODO agregar sentido de la ruta y entre calles

class FormPadre(models.Model):
    
    idAlarma = models.CharField(max_length=50, primary_key=True)
    tipo = models.CharField(max_length=30)
    hora = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length=50)
    altura = models.IntegerField()
    referencia = models.CharField(max_length=100)
    nombre = models.CharField(max_length=35)
    telefono = models.CharField(max_length=15)
    
    class Meta:

        abstract = True
        verbose_name = 'FormPadre'
        verbose_name_plural = 'FormsPadres'

    def __str__(self):
        return str(self.idAlarma)
        pass


class AccidenteVehicular(FormPadre):

    sentido = models.CharField(max_length=15)
    cantVehiculos = models.IntegerField()
    cantPersonas = models.IntegerField()
    herido = models.CharField(max_length=20)
    corteTransito = models.BooleanField()
    servEmergencia = models.CharField(max_length=30)

    class Meta:

        verbose_name = 'FormPadre' 
        verbose_name_plural = 'FormsPadres'

    def __str__(self):
        return super().__str__()

class IncendioForestal(FormPadre):

    sentido = models.CharField(max_length=15)
    riesgoProp = models.BooleanField()
    edificios = models.IntegerField()
    servEmergencia = models.CharField(max_length=30)

    class Meta:

        verbose_name = 'Incendio Forestal'
        verbose_name_plural = 'Incendios Forestales'

    def __str__(self):
        return super().__str__()

class IncendioBaldio(FormPadre):

    entreCalles = models.CharField(max_length=30)
    riesgoProp = models.BooleanField()
    class Meta:

        verbose_name = 'Incendio de Baldio'
        verbose_name_plural = 'Incendios de Baldios'

    def __str__(self):
        return super().__str__()

class IncendioVivienda(FormPadre):

    entreCalles = models.CharField(max_length=30)
    estadoFuego = models.CharField(max_length=30)
    habitantes = models.CharField(max_length=20)
    localHabit = models.CharField(max_length=40) 
    pisos = models.IntegerField()
    material = models.CharField(max_length=30)
    espera = models.BooleanField()
    class Meta:

        verbose_name = 'Incendio de Vivienda'
        verbose_name_plural = 'Incendios de Viviendas'

    def __str__(self):
        return super().__str__()

class IncendioVehicular(FormPadre):

    humoLlamas = models.CharField(max_length=30)
    localOcup = models.BooleanField()
    gnc = models.CharField(max_length=20)
    riesgoProp = models.BooleanField()
    class Meta:

        verbose_name = 'Incendio de Baldio'
        verbose_name_plural = 'Incendios de Baldios'

    def __str__(self):
        return super().__str__()
