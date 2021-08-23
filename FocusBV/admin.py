from django.contrib import admin
from .models import *

# Register your models here.

class AccidenteVehicularAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor','claseAC')

class IncendioForestalAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')    

class IncendioViviendaAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')   


    

admin.site.register(AccidenteVehicular,AccidenteVehicularAdmin)
admin.site.register(IncendioForestal, IncendioForestalAdmin)
admin.site.register(IncendioBaldio)
admin.site.register(IncendioVehicular)
admin.site.register(IncendioVivienda, IncendioViviendaAdmin)
admin.site.register(IncendioElectrico)
admin.site.register(RescateAnimal)
admin.site.register(RescateCadaver)