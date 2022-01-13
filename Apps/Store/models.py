from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, PositiveIntegerField

# Create your models here.

class category_product_model(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_de_creacion =  models.DateTimeField(auto_now=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural= "Categorias"

    def __str__(self):
        return self.nombre

class productos_model(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='productos')
    categoria = models.ForeignKey(category_product_model, on_delete=CASCADE)
    fecha_de_creacion =  models.DateTimeField(auto_now=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural= "Productos"

    def __str__(self):
        return self.nombre
