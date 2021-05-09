from django.db import models

# Create your models here.

class Person(models.Model):

    dni = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.dni)

class Form(models.Model):
# abstract
    formID = models.CharField(max_length=50, primary_key=True)
    date = models.DateField()
    hour = models.TimeField()
    alarmNumber = models.IntegerField()
    class Meta:
        
        abstract = True
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'
    

    def __str__(self):
        return str(self.formID)


class Car(models.Model):
   
    numberPlate = models.CharField(max_length=15, primary_key=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    color = models.CharField(max_length=20)
    damage = models.CharField(max_length=30)

    def __str__(self):
        return str(self.numberPlate)
    

class CarAccidentForm(Form):

    victims = models.BooleanField()
    description = models.CharField(max_length=300)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Accidente de Auto'
        verbose_name_plural = 'Accidentes de Autos'

    def __str__(self):
        return super().__str__()


'''
class somethingForm(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

class somethingForm(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

class somethingForm(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

class somethingForm(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

'''