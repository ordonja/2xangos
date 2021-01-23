
from django.forms.models import inlineformset_factory
from .models import Certificacion, CriterioProyecto, RequerimientoProyecto
CriterioFormset= inlineformset_factory(
    Certificacion, CriterioProyecto ,fields=('cumple', 'puntos_obtenidos',
    'indicadores', 'requerimientos', 'evidencias',),  can_delete=False,
)

RequerimientoFormset= inlineformset_factory(
    Certificacion, CriterioProyecto, fields=('cumple',))

def set_extra_forms(FormSet, extra_forms, **kwargs):
    FormSet= inlineformset_factory(
        Base , Inline, fields=('cumple',), can_delete=False,
        extra=extra_forms)
    return FormSet(**kwargs)
