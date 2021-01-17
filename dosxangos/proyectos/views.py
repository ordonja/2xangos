from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

from .models import Proyecto


def actualiza_proyectos(request):
    proyectos_todos = {}
    url = 'https://sigea.teamwork.com/projects.json?'
    response = requests.get(url)
    data = response.json()
    proyectos = data

#        for i in proyectos:
#            if i['status']=='active':
#                activo = True
#            datos_proyecto = Proyecto(
#            nombre = i['name'],
#            fk_predio = i['category.id'],
#            stampcrea = i['created-on'],
#            activo=activo,
#            descripcion = i['description'],
#            cliente = i['company'],)
#            datos_proyecto.save()
#            proyectos_todos = Proyecto.objects.all().order_by(-fk_tipo)
    return render (request, 'proyectos/tw.html', {'proyectos_todos':proyectos})

class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto


class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto


class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    fields = ['nombre', 'clave', 'fk_tipo', 'cliente', 'descripcion',
    'fechainicio', 'fk_proyectopadre', 'fk_predio', 'miembros']

    def get_success_url(self):
        return reverse('proyectos')
