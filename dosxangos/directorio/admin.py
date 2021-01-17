from django.contrib import admin
from dosxangos.directorio.models import *



class DireccionAdmin(admin.ModelAdmin):
    model = Direccion


class PersonaAdmin(admin.ModelAdmin):
    model = Persona


class CompanhiaAdmin(admin.ModelAdmin):
    model = Companhia


class EstadoAdmin(admin.ModelAdmin):
    model = Estado

class PaisAdmin(admin.ModelAdmin):
    model = Pais




admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Companhia,CompanhiaAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(Pais,PaisAdmin)
