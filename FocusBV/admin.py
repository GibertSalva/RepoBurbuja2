from django.contrib import admin
from .models import *

# Register your models here.

class AccidenteVehicularAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor','claseAC')



    

admin.site.register(AccidenteVehicular,AccidenteVehicularAdmin)
admin.site.register(IncendioForestal)
admin.site.register(IncendioBaldio)
admin.site.register(IncendioVehicular)
admin.site.register(IncendioVivienda)
admin.site.register(IncendioElectrico)
admin.site.register(RescateAnimal)
admin.site.register(RescateCadaver)