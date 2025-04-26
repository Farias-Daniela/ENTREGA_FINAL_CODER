from django.shortcuts import render, get_object_or_404
from .models import Destino

def listado_destinos(request):
    destinos = Destino.objects.all() #traer los destinos
    return render(request, "destinos/listado_destinos.html", {"destinos": destinos}) #vista de todos los destinos de la base de datos con destino.objec.all. los pasa al templatelistado_destinos,html

def detalle_destino(request, id):
    destino = get_object_or_404(Destino, id=id)
    return render(request, 'destinos/detalle_destino.html', {'destino': destino})

# Create your views here.
