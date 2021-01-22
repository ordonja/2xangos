from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

from .models import Certificacion, Criterio, CriterioProyecto
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

class CertificacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Certificacion
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['criterios'] = CriterioProyecto.objects.filter(fk_proyecto=self.object)
        return context


class CertificacionListView(LoginRequiredMixin, ListView):
    model=Certificacion
