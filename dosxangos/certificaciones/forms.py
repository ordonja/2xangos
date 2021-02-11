from django.forms import ModelForm, Textarea, TextInput, CharField
from django.forms.models import inlineformset_factory
from .models import Certificacion, CriterioProyecto, RequerimientoProyecto, Requerimiento


class CriterioProyectoForm(ModelForm):
    class Meta:
        model = CriterioProyecto
        fields=['cumple', 'puntos_obtenidos']


class RequerimientoProyectoLineForm(ModelForm):

    fk_req = CharField(disabled=True)


    class Meta:
        model = RequerimientoProyecto
        fields =['fk_req','cumple']

    # def __init__ (self, title, *args, **kwargs):
    #     init=super().get_context_data(**kwargs)
    #
    #     self.titulo = title
    #     super (RequerimientoProyectoLineForm, self).__init__ (*args, **kwargs) # call base clas
    #     name = 'caca'

# CriterioFormset= inlineformset_factory(
#     Certificacion, CriterioProyecto ,fields=('cumple', 'puntos_obtenidos',
#     'indicadores', 'requerimientos', 'evidencias',),  can_delete=False,
# )
#
# RequerimientoFormset= inlineformset_factory(
#     CriterioProyecto, RequerimientoProyecto, fields=('cumple','fk_req'), widgets={'fk_req': Textarea(attrs={'readonly': 'readonly'})})
#


RequerimientoFormSet = inlineformset_factory(
CriterioProyecto , RequerimientoProyecto, form=RequerimientoProyectoLineForm,
fields=('fk_req','cumple'), can_delete=False, extra=0)
