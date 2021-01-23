from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import inlineformset_factory

import requests

from .models import Certificacion, Criterio, CriterioProyecto, RequerimientoProyecto
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


class CriterioDetailView(LoginRequiredMixin, DetailView):
    model = Criterio


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
        context['criterios'] = CriterioProyecto.objects.filter(fk_criterio__clave__startswith='O', fk_proyecto=self.object)
        return context

class CertificacionVoluntarioDetailView(LoginRequiredMixin, DetailView):
    model=Certificacion
    template = 'certificacion_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['criterios'] = CriterioProyecto.objects.filter(fk_criterio__clave__startswith='V', fk_proyecto=self.object)
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
        context['criterios'] = CriterioProyecto.objects.filter(fk_criterio__clave__startswith='O', fk_proyecto=self.object)
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

class CertificacionVoluntarioUpdateView(LoginRequiredMixin, UpdateView):
    model=Certificacion
    template = 'certificacion_form.html'
    fields=['proyecto', 'criterios']
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['criterios'] = CriterioProyecto.objects.filter(fk_criterio__clave__startswith='V', fk_proyecto=self.object)
        return context

    def get_success_url(self):
            return reverse('detalles_cert', kwargs={'slug':self.object.slug})


class CertificacionListView(LoginRequiredMixin, ListView):
    model=Certificacion


class CriterioProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterioProyecto
    fields=['cumple', 'puntos_obtenidos',]

    def get_success_url(self):
            return reverse('certificaciones:detalles_crit_proy', kwargs={'pk':self.object.id})

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        req_num = RequerimientoProyecto.objects.filter(fk_criterio_proyecto=self.object.id).count()
        Form = inlineformset_factory(CriterioProyecto, RequerimientoProyecto, fields=('cumple',), can_delete=False, extra=(req_num+1))
        if self.request.POST:
            context['requerimientos']=Form(self.request.POST)
        else:
            context['requerimientos'] = Form()
        return context


class MetaListView(LoginRequiredMixin, ListView):
    model=Criterio
    template = 'criterio_list.html'

    queryset= Criterio.objects.prefetch_related('metas')
