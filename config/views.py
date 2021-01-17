from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView

from dosxangos.proyectos.models import *

@login_required
def index(request):
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        proyectos = Proyecto.objects.all()
        context = {
        'proyectos': proyectos,
        'user': user
        }
        #template = 'index.html'
        return render(request,'index.html', context)
    return render(request, 'index.html', context)


def twredirect(request):
    return redirect()

def index(request):
    proyectos = Proyecto.objects.all()
    context = {
        'proyectos': proyectos,
        }
    return render(request, 'index.html', context)

def registro(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            xango = form.save()
            login(request,xango)
            return render(request, 'index.html')
    context['form']=form
    return render(request, 'directorio/registro.html', context)
