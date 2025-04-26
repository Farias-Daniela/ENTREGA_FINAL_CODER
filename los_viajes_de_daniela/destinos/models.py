from django.db import models
from ckeditor.fields import RichTextField

class Destino(models.Model):
    titulo = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='destinos/')
    fecha = models.DateField()

    def __str__(self):
        return f"{self.titulo} - {self.pais}"
