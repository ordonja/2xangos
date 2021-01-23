from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProyectoListView.as_view(), name='proyectos'),
    path('nuevo', views.ProyectoCreateView.as_view(), name='nuevo'),
    path('tw/', views.actualiza_proyectos, name='tw'),
    path('<slug:slug>/', views.ProyectoDetailView.as_view(), name='detalles'),
    path('<slug:slug>/actualiza', views.ProyectoUpdateView.as_view(), name='actualiza'),
]
