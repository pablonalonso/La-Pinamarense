from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class categories_model(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_creacion =  models.DateTimeField(auto_now=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural= "Categorias"

    def __str__(self):
        return self.nombre

class posts_model(models.Model):
    nombre = models.CharField(max_length=500)
    contenido = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='')
    fecha_de_creacion =  models.DateTimeField(auto_now=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(categories_model)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural= "Posts"

    def __str__(self):
        return self.nombre


