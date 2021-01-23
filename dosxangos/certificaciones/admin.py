from django.contrib import admin
from dosxangos.certificaciones.models import *


class MetaInline(admin.TabularInline):
    model = Criterio.metas.through
    extra = 1

class CriterioProyectoInline(admin.TabularInline):
    model = CriterioProyecto
    extra = 1

class EvidenciaProyectoInline(admin.TabularInline):
    model = EvidenciaProyecto
    extra = 1

class RequerimientoProyectoInline(admin.TabularInline):
    model = RequerimientoProyecto
    extra = 1

class IndicadorProyectoInline(admin.TabularInline):
    model = IndicadorProyecto
    extra = 1

class RubroAdmin(admin.ModelAdmin):
    model = Rubro

class MetaAdmin(admin.ModelAdmin):
    model = Meta

class CriterioAdmin(admin.ModelAdmin):
    model = Criterio
    inlines = (MetaInline,)

class EvidenciaReqAdmin(admin.ModelAdmin):
    model = EvidenciaReq

class EvidenciaCriterioAdmin(admin.ModelAdmin):
    model = EvidenciaCriterio


class CertificacionAdmin(admin.ModelAdmin):
    model = Certificacion
    slug = 'proyecto__slug'
    inlines = (CriterioProyectoInline,)


class CriterioProyectoAdmin(admin.ModelAdmin):
    model = CriterioProyecto

    exclude=['fk_obs', ]


class EvidenciaProyectoAdmin(admin.ModelAdmin):
    model = EvidenciaProyecto


class IndicadorProyectoAdmin(admin.ModelAdmin):
    model = IndicadorProyecto


class RequerimientoProyectoAdmin(admin.ModelAdmin):
    model = RequerimientoProyecto


class IndicadorAdmin(admin.ModelAdmin):
    model = Indicador


admin.site.register(Rubro,RubroAdmin)
admin.site.register(Criterio,CriterioAdmin)
admin.site.register(EvidenciaCriterio,EvidenciaCriterioAdmin)
admin.site.register(Certificacion,CertificacionAdmin)
admin.site.register(CriterioProyecto,CriterioProyectoAdmin)
admin.site.register(EvidenciaProyecto, EvidenciaProyectoAdmin)
admin.site.register(RequerimientoProyecto, RequerimientoProyectoAdmin)
admin.site.register(IndicadorProyecto,IndicadorProyectoAdmin)
admin.site.register(EvidenciaReq, EvidenciaReqAdmin)
admin.site.register(Indicador, IndicadorAdmin)
admin.site.register(Meta, MetaAdmin)
