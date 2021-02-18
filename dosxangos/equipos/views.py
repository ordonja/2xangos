from django.shortcuts import render
# from django.urls import reverse
from django.views.generic import ListView
# , DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

import requests

from .models import EquipoProyecto


class EquipoProyectoListView(LoginRequiredMixin, ListView):
    model = EquipoProyecto
