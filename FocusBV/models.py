from django.db import models

# Create your models here.

class Person(models.Model):

    dni = models.IntegerField(max_leangth=8, primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.dni)

class Form(models.Model):

    formID = models.CharField(max=50, primary_key=True)
    date = models.DateField()
    hour = models.TimeField()
    alarmNumber = models.IntegerField(max=10)
    person = models.ManyToManyField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.formID)


class Car(models.Model):
   
    numberPlate = model.CharField(max=15, primary_key=True)
    brand = models.CharField(max=15)
    model = models.CharField(max=15)
    color = models.CharField(max=20)
    damage = models.CharField(max=30)

    def __str__(self):
        return str(self.numberPlate)
    

class CarAccidentForm(models.Model):

    victims = models.BooleanField()
    description = models.CharField(max_length=300)
    car = models.ManyToManyField(Car, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)



// SECTION
// TODO 

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


// !SECTION
