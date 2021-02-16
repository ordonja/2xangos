from django.forms import ModelForm, Textarea, TextInput, CharField
from django.forms.models import inlineformset_factory
from .models import CriterioProyecto, RequerimientoProyecto, EvidenciaProyecto


class RequerimientoProyectoLineForm(ModelForm):

    class Meta:
        model = RequerimientoProyecto
        fields =['cumple',]

class EvidenciaProyectoLineForm(ModelForm):

    class Meta:
        model = EvidenciaProyecto
        fields =['cumple', 'evidencia_presentada', 'fk_obs',]


RequerimientoFormSet = inlineformset_factory(
CriterioProyecto, RequerimientoProyecto, form=RequerimientoProyectoLineForm,
fields=('cumple',), can_delete=False, extra=0)

EvidenciaFormSet = inlineformset_factory(
CriterioProyecto, EvidenciaProyecto, form=EvidenciaProyectoLineForm,
fields=('cumple', 'evidencia_presentada', 'fk_obs',), can_delete=False, extra=0)
