from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RequerimientoFormSet, CriterioProyectoForm

import requests

from .models import Certificacion, Criterio, CriterioProyecto, RequerimientoProyecto, Requerimiento
# def get_requerimientos(request):
#     requerimientos = Requerimiento
# def index(request):
#     if request.user.is_authenticated():
#         user = User.objects.get(id=request.user.id)
#         proyectos = Proyecto.objects.all()
#         context = {
#         'proyectos': proyectos,
#         'user': user
#         }
#         #template = 'index.html'
#         return render(request,'index.html', context)
#     return render(request, 'index.html', context)



class CriterioListView(LoginRequiredMixin, ListView):
    model = Criterio
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['crit_ob'] = Criterio.objects.filter(clave__startswith='O')
        context['crit_vol'] = Criterio.objects.filter(clave__startswith='V')
        return context


class CriterioProyectoDetailView(LoginRequiredMixin, DetailView):
    model = CriterioProyecto


class CertificacionDetailView(LoginRequiredMixin, DetailView):
    model=Certificacion
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['criterios'] = CriterioProyecto.objects.filter(fk_proyecto=self.object)
        return context

class CertificacionObligaDetailView(LoginRequiredMixin, DetailView):
    model=Certificacion
    template = 'certificacion_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['criterios']= CriterioProyecto.objects.filter(fk_criterio__obligatorio_dc=True, fk_proyecto=self.object).prefetch_related('evidencias', 'indicadores','requerimientos')
        print(context['criterios'])
        return context

class CertificacionVoluntarioDetailView(LoginRequiredMixin, DetailView):
    model=Certificacion
    template = 'certificacion_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

class CertificacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Certificacion
    fields=['proyecto', 'criterios']

    def get_success_url(self):
        return reverse('detalles_cert', kwargs={'slug':self.object.slug})


class CertificacionObligaUpdateView(LoginRequiredMixin, UpdateView):
    model=Certificacion
    template = 'certificacion_form.html'
    fields=['proyecto', 'criterios']

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['criterios']= CriterioProyecto.objects.prefetch_related('evidencias','indicadores','requerimientos').filter(fk_criterio__obligatorio_dc=True)

        print(context['criterios'])
        if self.request.POST:
            context['criterios'] = CriterioFormset(self.request.POST)
        else:
            context['criterios'] = CriterioFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        criterios = context['criterios']
        self.object = form.save()
        if criterios.is_valid():
            criterios.instance = self.objects
            criterios.save()
        return super().form_valid(form)

    def get_success_url(self):
            return reverse('detalles_cert', kwargs={'slug':self.object.slug})


class CertificacionListView(LoginRequiredMixin, ListView):
    model=Certificacion


class CriterioProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterioProyecto
    form_class = CriterioProyectoForm

    def get_success_url(self):
        return reverse('certificaciones:detalles_crit_proy', kwargs={'pk':self.object.id})

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        criterio_proyecto = CriterioProyecto.objects.get(id=self.object.id)
        context['requerimientos'] = criterio_proyecto.requerimientoproyecto_set.all().select_related('fk_req')
        print(context['requerimientos'])
        if self.request.POST:
            context['formset'] = RequerimientoFormSet(self.request.POST, instance=criterio_proyecto)
        else:
            context['formset'] = RequerimientoFormSet(instance=criterio_proyecto)
        return context


    # def manage_requerimientos(self, request, criterio_proyecto_id):
    #     criterio_proyecto = CriterioProyecto.objects.get(id=criterio_proyecto_id)
    #     print(criterio_proyecto)
    #     if request.method == "POST":
    #         formset = RequerimientoFormSet(self.request.POST, instance=criterio_proyecto)
    #     else:
    #         formset = Form(instance=criterio_proyecto)
    #
    #         if formset.is_valid():
    #             formset.save()
    #             return reverse('certificaciones:detalles_crit_proy', kwargs={'pk':self.object.id})
    #     else:
    #         formset = RequerimientoFormSet(instance=criterio_proyecto)
        # return render(request, 'criterioproyecto_form.html', {'formset':formset})


class CriterioDetailView(LoginRequiredMixin, DetailView):
    model = Criterio
    queryset= Criterio.objects.prefetch_related('evidencias', 'metas','indicadores','requerimientos')
