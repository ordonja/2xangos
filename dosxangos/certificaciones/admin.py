from django.contrib import admin
from dosxangos.certificaciones.models import *


class RubroAdmin(admin.ModelAdmin):
    model = Rubro


class CriterioAdmin(admin.ModelAdmin):
    model = Criterio


class EvidenciaCriterioAdmin(admin.ModelAdmin):
    model = EvidenciaCriterio


class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto


class CriterioProyectoAdmin(admin.ModelAdmin):
    model = CriterioProyecto


class EvidenciaReqAdmin(admin.ModelAdmin):
    model = EvidenciaReq


class EvidenciaCriterioProyAdmin(admin.ModelAdmin):
    model = EvidenciaCriterioProy


admin.site.register(EvidenciaCriterioProy, EvidenciaCriterioProyAdmin)
admin.site.register(EvidenciaReq, EvidenciaReqAdmin)
admin.site.register(CriterioProyecto,CriterioProyectoAdmin)
admin.site.register(EvidenciaCriterio,EvidenciaCriterioAdmin)
admin.site.register(Criterio,CriterioAdmin)
admin.site.register(Rubro,RubroAdmin)
