from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RequerimientoFormSet, EvidenciaFormSet

import requests

from .models import (Certificacion, Criterio, CriterioProyecto, RequerimientoProyecto,
Requerimiento, EvidenciaProyecto, Indicador)


class CriterioProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterioProyecto
    fields=['puntos_obtenidos', 'cumple', 'fk_obs',]

    def get_success_url(self):
        return reverse('certificaciones:detalles_crit_proy', kwargs={'pk':self.object.id})

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        criterio_proyecto = CriterioProyecto.objects.get(id=self.object.id)
        if self.request.POST:
            requerimiento_formset = RequerimientoFormSet(self.request.POST, instance=criterio_proyecto, prefix='requerimientos')
            evidencia_formset = EvidenciaFormSet(self.request.POST, instance=criterio_proyecto, prefix='evidencias')
        else:
            requerimiento_formset = RequerimientoFormSet(instance=criterio_proyecto, prefix='requerimientos')
            evidencia_formset = EvidenciaFormSet(instance=criterio_proyecto, prefix='evidencias')
        context['requerimiento_formset'] = requerimiento_formset
        context['evidencia_formset'] = evidencia_formset

        if evidencia_formset.is_valid() and requerimiento_formset.is_valid():
            self.object = form.save()
            evidencia_formset.instance = self.object
            evidencia_formset.save()
            requerimiento_formset.instance = self.object
            requerimiento_formset.save()
        return context


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
        context['obligatorios'] = self.object.get_criterios_obligatorios()
        context['voluntarios'] = self.object.get_criterios_voluntarios()
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


class CriterioDetailView(LoginRequiredMixin, DetailView):
    model = Criterio
    queryset= Criterio.objects.prefetch_related('evidencias', 'metas','indicadores','requerimientos')


class IndicadorListView(LoginRequiredMixin, ListView):
    model = Indicador
