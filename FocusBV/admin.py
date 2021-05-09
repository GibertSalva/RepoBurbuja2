from django.contrib import admin
from .models import *

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Data', {
          'fields': ('dni','name','surname',)  
        }),
        ('Extra', {
            'fields': ('phone','address',)
        }),
    )
    list_display = ['dni','name','surname','phone','address',]
    list_display_links = ['dni','name','surname','phone','address',]
    search_fields = ['dni','name','surname','phone','address',]


class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Data', {
          'fields': ('numberPlate','brand','model',)  
        }),
        ('Extra', {
            'fields': ('color','damage',)
        }),
    )
    list_display = ['numberPlate','brand','model','color','damage',]
    list_display_links = ['numberPlate','brand','model','color','damage',]
    search_fields = ['numberPlate','brand','model','color','damage',]


class CarAccidentFormAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Data', {
          'fields': ('formID', 'date','hour','alarmNumber','victims','description','car',)  
        }),
    )
    list_display = ['formID', 'date','hour','alarmNumber','victims','description','car',]
    list_display_links = ['formID', 'date','hour','alarmNumber','victims','description','car',]
    search_fields = ['formID', 'date','hour','alarmNumber','victims','description','car',]

    

admin.site.register(Person, PersonAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarAccidentForm, CarAccidentFormAdmin)