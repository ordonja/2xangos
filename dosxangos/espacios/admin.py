from django.contrib import admin
from dosxangos.espacios.models import *


class SuperficieInline(admin.TabularInline):
    model = Superficie
    extra = 1


class EspacioInline(admin.TabularInline):
    model = Espacio
    extra = 1

class SuperficieAdmin(admin.ModelAdmin):
    model = Superficie
    #inlines = (BrigadaInline,)


class EspacioAdmin(admin.ModelAdmin):
    model = Espacio
    inlines = (SuperficieInline,)


class PredioAdmin(admin.ModelAdmin):
    model = Predio


class ZonificacionAdmin(admin.ModelAdmin):
    model = Zonificacion


class EdificioAdmin(admin.ModelAdmin):
    model =Edificio
    inlines = (EspacioInline,)

admin.site.register(Superficie, SuperficieAdmin)
admin.site.register(Espacio,EspacioAdmin)
admin.site.register(Predio,PredioAdmin)
admin.site.register(Zonificacion,ZonificacionAdmin)
admin.site.register(Edificio,EdificioAdmin)
