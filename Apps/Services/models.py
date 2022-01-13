from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.

class services_model(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='')
    fecha_de_creacion =  models.DateTimeField(auto_now=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural= "Servicios"

    def __str__(self):
        return self.titulo

