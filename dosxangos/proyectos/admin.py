from django.contrib import admin
from dosxangos.proyectos.models import *


class BrigadaInline(admin.TabularInline):
    model = Brigada
    extra = 1


class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto
    inlines = (BrigadaInline,)


class TipoProyectoAdmin(admin.ModelAdmin):
    model = TipoProyecto


class AreasproyAdmin(admin.ModelAdmin):
    model = Areasproy


class ObsAdmin(admin.ModelAdmin):
    model = Obs


class BrigadaAdmin(admin.ModelAdmin):
    model = Brigada
    extra = 1


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(TipoProyecto,TipoProyectoAdmin)
admin.site.register(Areasproy,AreasproyAdmin)
admin.site.register(Obs,ObsAdmin)
admin.site.register(Brigada,BrigadaAdmin)
