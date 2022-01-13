from django.shortcuts import render
from .models import category_product_model, productos_model
from Apps.ShoppingCart.carro import shopping_cart



# Create your views here.

def store(request):
    all_products = productos_model.objects.all()
    all_product_categories = category_product_model.objects.all()
    carro = request.session.get("shoppingcart")
    print(carro)
    return render(request, 'store.html', {
        "all_products_key": all_products,
        "all_product_categories_key": all_product_categories,
        "carro_key": carro,
    })


def productos_filtrados(request, cat_prod_id):
    category_filter = category_product_model.objects.get(id=cat_prod_id)
    all_products_filtered = productos_model.objects.filter(categoria=category_filter)
    return render(request, 'filtro_product.html', {
        "category_product_filter_key": category_filter,
        "all_products_filtered_key": all_products_filtered,
    })

