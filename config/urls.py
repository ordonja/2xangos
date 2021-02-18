"""dosxangos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='home'),
#    path('static/', dosxangos.static, name = static),

    path('bandar-log/', admin.site.urls),
    path('registro/', views.registro, name='registro'),
    path('inicio/', auth_views.LoginView.as_view(), name='inicio'),
    path('cierre/', auth_views.LogoutView.as_view(), name='cierre'),

    path('cambia_contraseña/', auth_views.PasswordChangeView.as_view(), name='cambia_contraseña'),
    path('contraseña_cambiada/', auth_views.PasswordChangeDoneView.as_view(), name='contraseña_cambiada'),
    path('restablecer_contraseña/', auth_views.PasswordResetView.as_view(), name='restablecer_contraseña'),
    path('contraseña_restablecida/', auth_views.PasswordResetDoneView.as_view(), name='contraseña_restablecida'),
    path('restablece/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='confirma_restablece'),
    path('restablece_listo/', auth_views.PasswordResetCompleteView.as_view(), name='restablece_listo'),

    path('proyectos/', include('dosxangos.proyectos.urls'), name ='proyectos'),
    path('cert/', include('dosxangos.certificaciones.urls'), name ='certificaciones'),
    path('equipos/', include('dosxangos.equipos.urls'), name ='equipos'),
    #ProyectoListView.as_view(), name='lista'),
    #path(route='<slug:nombre>', view=views.ProyectoDetailView.as_view(), name='detalle'),
    #path(route='<slug:nombre>/update/', view=views.ProyectoUpdateView.as_view(), name='update')
]
