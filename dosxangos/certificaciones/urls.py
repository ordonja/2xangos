from django.urls import path
from . import views


urlpatterns = [
    path('', views.CertificacionListView.as_view(), name='certificaciones'),
    path('criterios/', views.CriterioListView.as_view(), name='criterios'),
    path('criterio/<int:id>/', views.CriterioDetailView.as_view(), name='detalles'),
    path('<slug:slug>/', views.CertificacionDetailView.as_view(), name='detalles_cert'),
    path('<slug:slug>/actualiza', views.CertificacionUpdateView.as_view(), name='actualiza_cert'),
    path('criteriop/<int:id>', views.CriterioProyectoDetailView.as_view(), name='detalles_crit_proy'),

    ]
