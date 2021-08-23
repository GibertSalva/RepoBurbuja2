from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField
from django.forms import ModelForm


# Create your models here.
# TODO agregar sentido de la ruta y entre calles

class FormPadre(models.Model):
    
    idAlarma = models.AutoField(primary_key=True)
    hora = models.TimeField()
    receptor = models.CharField(max_length=50)
    nombre = models.CharField(max_length=35)
    telefono = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    referencia = models.TextField(max_length=100, null=True)
    
    class Meta:

        abstract = True
        verbose_name = 'Formulario Padre'
        verbose_name_plural = 'Formularios Padres'

    def __str__(self):
        return str(self.idAlarma)


class AccidenteVehicular(FormPadre):# 20-20
    tipoAV = [
        ('A','Automovil'),
        ('B','Omnibus'),
        ('C','Camion'),
        ('D','Motocicleta'),
        ('E','Atropellado')
    ]

    tiposC = [
        ('C','Calle'),
        ('A','Acenida'),
        ('R','Ruta'),
        ('U','Undefined')
    ]
    claseAC = models.CharField(max_length=10,choices=tipoAV,default=None)
    cantVehiculos = models.IntegerField()
    cantPersonas = models.IntegerField()
    corteTransito = models.BooleanField()
    tipoCalle = models.CharField(max_length=10,choices=tiposC,default='U')
    herido = models.CharField(max_length=20)
    servEmergencia = models.CharField(max_length=30)

    class Meta:

        verbose_name = 'Accidente Vehicular' 
        verbose_name_plural = 'Accidentes Vehiculares'

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
    descVivienda = models.CharField(max_length=50)
    espera = models.BooleanField()
    class Meta:

        verbose_name = 'Incendio de Vivienda'
        verbose_name_plural = 'Incendios de Viviendas'

    def __str__(self):
        return super().__str__()

class IncendioVehicular(FormPadre):

    tipoVehiculo = models.CharField(max_length=20)
    humoLlamas = models.CharField(max_length=30)
    localOcup = models.BooleanField()
    gnc = models.CharField(max_length=20)
    riesgoProp = models.BooleanField()
    class Meta:

        verbose_name = 'Incendio Vehicular'
        verbose_name_plural = 'Incendios Vehiculares'

    def __str__(self):
        return super().__str__()

class IncendioElectrico(FormPadre):

    desperfecto = models.CharField(max_length=30)
    humoLlamas = models.CharField(max_length=30)
    epec = models.CharField(max_length=30)
    servEmergencia = models.CharField(max_length=30)
    class Meta:

        verbose_name = 'Incendio Electrico'
        verbose_name_plural = 'Incendios Electricos'

    def __str__(self):
        return super().__str__()


class RescateAnimal(FormPadre):

    animal = models.CharField(max_length=15)
    condicionAnimal = models.CharField(max_length=30)
    vision = models.BooleanField()

    class Meta:

        verbose_name = 'Rescate Animal'
        verbose_name_plural = 'Rescate de Animales'

    def __str__(self):
        return super().__str__()

class RescateCadaver(FormPadre):
    esPolicia = models.BooleanField()
    #* Datos diferentes dependiendo si el que llamos es policia o civil
    cantPolicia: models.IntegerField()
    motivoMuerte: models.CharField(max_length=30)
    estadoCadaver : models.CharField(max_length=35)
    #* var estadoCadaver incluye si esta descompuesto, localizacion del cuerpo y la posicion
    #* Datos exclusivos para la Policia:
    certDefuncion: models.BooleanField()
    remocion: models.CharField(max_length=30)
    seguroBomb: models.BooleanField()

    class Meta:

        verbose_name = 'Rescate de Cadaver'
        verbose_name_plural = 'Rescates de Cadaveres'

    def __str__(self):
        return super().__str__()




