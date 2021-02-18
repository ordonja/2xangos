from django.urls import path
from . import views
app_name = "equipos"

urlpatterns = [
    path('<slug:slug>/equipos', views.EquipoProyectoListView.as_view(), name='equipos_proy'),
]
