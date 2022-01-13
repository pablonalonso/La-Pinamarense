from django.contrib import admin
from .models import  productos_model, category_product_model

# Register your models here.

class categoryProductoAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_de_creacion', 'ultima_actualizacion')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_de_creacion', 'ultima_actualizacion')




admin.site.register(productos_model, ProductoAdmin)
admin.site.register(category_product_model, categoryProductoAdmin)


