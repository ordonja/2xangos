from django.contrib import admin
from django import forms
from django.conf.urls import re_path
from django.utils.translation import ugettext as _

from dosxangos.equipos.models import *

class SubclassFilter(admin.SimpleListFilter):
    title = _('tipo')
    parameter_name = 'tipo'

    def lookups(self, request, model_admin):
        return Equipo.SUBCLASS_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.exclude(**{self.value(): None})
        return queryset




@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    model = Equipo
    list_display =  [
    'tipo',
    'equipo_tipo',
    'marca',
    'modelo',
    'potencia',
    'unidad_potencia',
    'eficiencia',
    'fuente_ener',
    'equipo_padre',
    'pais_origen',
    'ficha_tec',
    'url_ft',
    'anho_fabricacion',
    ]
    list_filter = [SubclassFilter]

    def get_queryset(self, request):
        return super(EquipoAdmin, self).get_queryset(request).select_subclasses()

    def tipo(self, obj):
        return obj._meta.verbose_name

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            Model = Equipo
            Model = Equipo.SUBCLASS(request.GET.get('tipo'))
        else:
            Model = obj.__class__

            #When we change the selected gender in the create form, we want to reload the page.
        RELOAD_PAGE = "window.location.search='?tipo='+ this.value"
        #We should also grab all existing field values, and pass them as query string values.

        class ModelForm(forms.ModelForm):
            if not obj:
                tipo = forms.ChoiceField(
                    help_text=_('Por favor escoge...'),

                    choices= Equipo.CLASS_CHOICE + Equipo.SUBCLASS_CHOICES,
                    widget=forms.Select(attrs={'onchange': RELOAD_PAGE})
                )

            class Meta:
                model = Model
                exclude = ()

        return ModelForm

    def get_fields(self, request, obj=None):
        #We eant tipo_eq to be the first field.
        fields = super(EquipoAdmin, self).get_fields(request, obj)

        if 'tipo' in fields:
            fields.remove('tipo')
            fields = ['tipo'] + fields
        return fields

    # def get_urls(self):
    #     #We want to install name durls that match the subclass ones, but bounce to the
    #     #relevant superclass ones, since they should be able to handle rendering the correct form.
    #     urls = super(EquipoAdmin, self).get_urls()
    #     print(urls)
    #     existing = '{}_{}_'.format(self.model._meta.app_label, self.model._meta.model_name)
    #     subclass_urls=[]
    #     for name, model in Equipo.SUBCLASS_OBJECT_CHOICES.items():
    #         opts = model._meta
    #         replace = '{}_{}_'.format(opts.app_label, opts.model_name)
    #         subclass_urls.extend([
    #             re_path('', pattern.callback, name=pattern.name.replace(existing, replace))
    #             for pattern in urls if pattern.name
    #         ])
    #     return urls + subclass_urls

class EquipoProyectoAdmin(admin.ModelAdmin):
    model = EquipoProyecto


class UnidadMedicionAdmin(admin.ModelAdmin):
    model = UnidadMedicion

class TipoEquipoAdmin(admin.ModelAdmin):
    model = TipoEquipo


class NormaEquipoAdmin(admin.ModelAdmin):
    model = NormaEquipo

class MotorAdmin(admin.ModelAdmin):
    model = MotorElectrico


admin.site.register(TipoEquipo,TipoEquipoAdmin)
admin.site.register(NormaEquipo,NormaEquipoAdmin)
admin.site.register(EquipoProyecto,EquipoProyectoAdmin)
admin.site.register(UnidadMedicion,UnidadMedicionAdmin)
admin.site.register(MotorElectrico,MotorAdmin)
