from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from .models import categories_model, posts_model

class categoriesAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_de_creacion','ultima_actualizacion')

class postsAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_de_creacion','ultima_actualizacion')

admin.site.register(categories_model, categoriesAdmin)
admin.site.register(posts_model, postsAdmin)
