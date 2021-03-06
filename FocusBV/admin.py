from django.contrib import admin
from .models import *

# Register your models here.


class AccidenteVehicularAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor','claseAC')


class IncendioForestalAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class IncendioBaldioAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class RescateAnimalAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class IncendioVehicularAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class PerdidaCombustibleAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class EscapeGasAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class RescatePersonaViaAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class IncendioViviendaAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class IncendioElectricoAdmin(admin.ModelAdmin):
    list_display = ('idAlarma','receptor')


class FormularioAuxiliarAdmin(admin.ModelAdmin):
    list_display = ('auxiliar',)


    

admin.site.register(AccidenteVehicular,AccidenteVehicularAdmin)
admin.site.register(IncendioForestal, IncendioForestalAdmin)
admin.site.register(IncendioBaldio,IncendioBaldioAdmin)
admin.site.register(RescateAnimal,RescateAnimalAdmin)
admin.site.register(IncendioVehicular,IncendioVehicularAdmin)
admin.site.register(IncendioVivienda, IncendioViviendaAdmin)
admin.site.register(IncendioElectrico, IncendioElectricoAdmin)
admin.site.register(PerdidaCombustible, PerdidaCombustibleAdmin)
admin.site.register(EscapeGas, EscapeGasAdmin)
admin.site.register(RescatePersonaVia, RescatePersonaViaAdmin)
admin.site.register(FormularioAuxiliar, FormularioAuxiliarAdmin)