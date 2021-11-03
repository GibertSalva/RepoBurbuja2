from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField
from django.forms import ModelForm
import datetime


# TODO agregar sentido de la ruta y entre calles

class FormPadre(models.Model):
    
    idAlarma = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today,null=True)
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

    def getUrl(self):
        return str(self.idAlarma)
    
    def getClass(self):
        return self._meta.verbose_name_raw

class IncendioForestal(FormPadre): #10-10

    sentido = models.CharField(max_length=15)
    riesgoProp = models.BooleanField() # Riesgo de Propagacion
    edificios = models.IntegerField()
    servEmergencia = models.CharField(max_length=30)

    class Meta:

        verbose_name = 'Incendio Forestal'
        verbose_name_plural = 'Incendios Forestales'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
        return str(self.idAlarma)

class IncendioBaldio(FormPadre): #10-11

    entreCalles = models.CharField(max_length=30)
    riesgoProp = models.BooleanField() # Riesgo de Propagacion
    class Meta:

        verbose_name = 'Incendio de Baldio'
        verbose_name_plural = 'Incendios de Baldios'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
            return str(self.idAlarma)

class IncendioVivienda(FormPadre): #10-13

    entreCalles = models.CharField(max_length=30)
    estadoFuego = models.CharField(max_length=30)
    habitantes = models.CharField(max_length=20)
    localHabit = models.CharField(max_length=40) # Hay habitantes en el momento? Cuantos?
    descVivienda = models.CharField(max_length=50) # Como es la vivienda?
    espera = models.BooleanField()
    class Meta:

        verbose_name = 'Incendio de Vivienda'
        verbose_name_plural = 'Incendios de Viviendas'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
        return str(self.idAlarma)

class IncendioVehicular(FormPadre): #10-14

    tipoVehiculo = models.CharField(max_length=20)
    humoLlamas = models.CharField(max_length=30)
    vehiculoOcup = models.BooleanField()
    gnc = models.CharField(max_length=20)
    riesgoProp = models.BooleanField() # Riesgo de Propagacion
    class Meta:

        verbose_name = 'Incendio Vehicular'
        verbose_name_plural = 'Incendios Vehiculares'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
        return str(self.idAlarma)

class PerdidaCombustible(FormPadre): # 10-16

    tipoCombustible = models.CharField(max_length=20)
    servEmergencia = models.CharField(max_length=30)
    hayVictimas = models.CharField(max_length=30)

    class Meta:

        verbose_name = 'Perdida de Combustible'
        verbose_name_plural = 'Perdidas de Combustible'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
        return str(self.idAlarma)

class EscapeGas(FormPadre): #10-17

    tipoIncidente = models.CharField(max_length=20) #vivienda, auto o via publica
    #AGREGAR INDICACIONES, probablemente sea simplemente un texto en el template.

    class Meta:

        verbose_name = 'Escape de Gas'
        verbose_name_plural = 'Escapes de Gas'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
        return str(self.idAlarma)

class IncendioElectrico(FormPadre): #10-19

    desperfecto = models.CharField(max_length=30)
    humoLlamas = models.CharField(max_length=30)
    epec = models.CharField(max_length=30)
    servEmergencia = models.CharField(max_length=30)
    class Meta:

        verbose_name = 'Incendio Electrico'
        verbose_name_plural = 'Incendios Electricos'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
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
        ('A','Avenida'),
        ('R','Ruta'),
        ('U','Undefined')
    ]
    claseAC = models.CharField(max_length=10,choices=tipoAV,default=None)
    cantVehiculos = models.CharField(max_length=200,blank=True)
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

    def getUrl(self):
        return str(self.idAlarma)

class RescateAnimal(FormPadre): #20-22

    animal = models.CharField(max_length=15)
    condicionAnimal = models.CharField(max_length=30)
    vision = models.BooleanField()

    class Meta:

        verbose_name = 'Rescate Animal'
        verbose_name_plural = 'Rescate de Animales'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
        return str(self.idAlarma)


class RescateCadaver(FormPadre): #20-23
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

    def getUrl(self):
        return str(self.idAlarma)

class RescatePersonaVia(FormPadre): #20-24

    estadoPersona = models.CharField(max_length=30)
    lesion = models.CharField(max_length=30)

    class Meta:
        
        verbose_name = 'Rescate de Persona en Via Publica'
        verbose_name_plural = 'Rescates de Personas en Via Publica'
    
    def getUrl(self):
        return str(self.idAlarma)

####FORMULARIO DE AUXILIO

class FormularioAuxiliar(FormPadre):

    auxiliar = models.CharField(max_length=200,blank=True)

    class Meta:

        verbose_name = 'Formulario Auxiliar'
        verbose_name_plural = 'Formularios Auxiliares'

    def __str__(self):
        return super().__str__()

    def getUrl(self):
        return str(self.idAlarma)
