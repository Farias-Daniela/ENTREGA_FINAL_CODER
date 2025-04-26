from django.db import models
from django.utils import timezone

class Destino(models.Model):
    titulo = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='destinos/')
    fecha = models.DateField(default=timezone.now, null=True, blank=True)  # Permite NULL y tiene valor por defecto

    def __str__(self):
        return self.titulo