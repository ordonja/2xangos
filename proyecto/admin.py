from django.contrib import admin
from proyecto.models import *



class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto


class TipoProyectoAdmin(admin.ModelAdmin):
    model = TipoProyecto


class AreasproyAdmin(admin.ModelAdmin):
    model = Areasproy


class ObsAdmin(admin.ModelAdmin):
    model = Obs



admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(TipoProyecto,TipoProyectoAdmin)
admin.site.register(Areasproy,AreasproyAdmin)
admin.site.register(Obs,ObsAdmin)
