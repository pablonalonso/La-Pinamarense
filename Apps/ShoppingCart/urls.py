from django.urls import path
from . import views

app_name = "cart"


urlpatterns = [
     path('agregar/<int:producto_id>/', views.agregar_producto, name='add'),
     path('eliminar/<int:producto_id>/', views.eliminar_producto, name='del'),
     path('restar/<int:producto_id>/', views.restar_producto, name='sub'),
     path('limpiar/', views.limpiar_carro, name='clean'),
]
