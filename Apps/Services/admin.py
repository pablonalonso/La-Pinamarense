from django.contrib import admin
from .models import services_model

# Register your models here.

class servicesAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_de_creacion','ultima_actualizacion')

admin.site.register(services_model, servicesAdmin)
