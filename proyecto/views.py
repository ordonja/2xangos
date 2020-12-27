from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
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
    return render (request, 'proyecto/tw.html', {'proyectos_todos':proyectos})


class ProyectoListView(ListView):
    model = Proyecto


class ProyectoDetailView(DetailView):
    model = Proyecto


class ProyectoUpdateView(UpdateView):
    model = Proyecto
# Create your views here.
