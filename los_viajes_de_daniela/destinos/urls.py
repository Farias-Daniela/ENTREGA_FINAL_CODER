from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_destinos, name='listado_destino'),  #muestra todos los destinos
    path('<int:id>/', views.detalle_destino, name='detalle_destino'),  # detalle de un destino específico
]

