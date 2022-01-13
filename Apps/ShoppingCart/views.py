from .carro import shopping_cart
from Apps.Store.models import productos_model
from django.shortcuts import redirect

def agregar_producto(request, producto_id):
    carro = shopping_cart(request)
    product_to_add= productos_model.objects.get(id=producto_id)
    carro.agregar(producto=product_to_add)
    return redirect("store")

def eliminar_producto(request, producto_id):
    carro = shopping_cart(request)
    product_to_add= productos_model.objects.get(id=producto_id)
    carro.eliminar(producto=product_to_add)
    return redirect("store")

def restar_producto(request, producto_id):
    carro = shopping_cart(request)
    product_to_add = productos_model.objects.get(id=producto_id)
    carro.restar_producto(producto=product_to_add)
    return redirect("store")

def limpiar_carro(request):
    carro = shopping_cart(request)
    carro.limpiar_carro()
    return redirect("store")







