from django.contrib import admin
from dosxangos.proyectos.models import *



class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto


class TipoProyectoAdmin(admin.ModelAdmin):
    model = TipoProyecto


class AreasproyAdmin(admin.ModelAdmin):
    model = Areasproy


class ObsAdmin(admin.ModelAdmin):
    model = Obs

class BrigadaAdmin(admin.ModelAdmin):
    model = Brigada




admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(TipoProyecto,TipoProyectoAdmin)
admin.site.register(Areasproy,AreasproyAdmin)
admin.site.register(Obs,ObsAdmin)
admin.site.register(Brigada,BrigadaAdmin)
