from django.urls import path
from . import views
app_name = "certificaciones"

urlpatterns = [
    path('', views.CertificacionListView.as_view(), name='certificaciones'),
#    path('metas/', views.MetaListView.as_view(), name='metas'),
    path('criteriobase/', views.CriterioListView.as_view(), name='criterios'),
    path('criteriobase/<int:pk>/', views.CriterioDetailView.as_view(), name='detalles_crit'),
#    path('criteriobase/<int:pk>/actualiza', views.CriterioUpdateView.as_view(), name='edita_crit'),
    path('criterio/<int:pk>/', views.CriterioProyectoDetailView.as_view(), name='detalles_crit_proy'),
    path('indicadores/', views.IndicadorListView.as_view(), name='indicadores'),
    path('criterio/<int:pk>/actualiza', views.CriterioProyectoUpdateView.as_view(), name='edita_crit_proy'),
    path('<slug:slug>/', views.CertificacionDetailView.as_view(), name='detalles_cert'),
    path('<slug:slug>/actualiza', views.CertificacionUpdateView.as_view(), name='edita_cert'),

#    path('<slug:slug>/o/actualiza', views.CertificacionObligaUpdateView.as_view(), name='edita_cert_obliga'),
#    path('<slug:slug>/v/actualiza', views.CertificacionVoluntarioUpdateView.as_view(), name='edita_cert_vol'),
]
