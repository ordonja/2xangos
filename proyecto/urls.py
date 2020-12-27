from django.urls import path


from . import views


urlpatterns = [
    path('', views.ProyectoListView.as_view()),
    path('tw/', views.actualiza_proyectos, name='tw'),
    path('<slug:slug>/', views.ProyectoDetailView.as_view(), name='detalles'),
]
