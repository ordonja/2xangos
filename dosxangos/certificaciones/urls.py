from django.urls import path
from . import views
app_name = "certificaciones"

urlpatterns = [
    path('', views.CertificacionListView.as_view(), name='certificaciones'),
    path('metas/', views.MetaListView.as_view(), name='metas'),
    path('criteriobase/', views.CriterioListView.as_view(), name='criterios'),
    path('criteriobase/<int:id>/', views.CriterioDetailView.as_view(), name='detalles'),
    path('criterio/<int:pk>', views.CriterioProyectoDetailView.as_view(), name='detalles_crit_proy'),
    path('criterio/<int:pk>/actualiza', views.CriterioProyectoUpdateView.as_view(), name='actualiza_crit_proy'),
    path('<slug:slug>/', views.CertificacionDetailView.as_view(), name='detalles_cert'),
    path('<slug:slug>/o/', views.CertificacionObligaDetailView.as_view(), name='detalles_cert_obliga'),
    path('<slug:slug>/v/', views.CertificacionVoluntarioDetailView.as_view(), name='detalles_cert_vol'),
    path('<slug:slug>/actualiza', views.CertificacionUpdateView.as_view(), name='actualiza_cert'),
    path('<slug:slug>/o/actualiza', views.CertificacionObligaUpdateView.as_view(), name='actualiza_cert_obliga'),
    path('<slug:slug>/v/actualiza', views.CertificacionVoluntarioUpdateView.as_view(), name='actualiza_cert_vol'),
]
