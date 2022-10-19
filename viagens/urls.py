from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name = 'index.html'),
    path('consulta', views.revConsulta, name = 'consulta'),
]