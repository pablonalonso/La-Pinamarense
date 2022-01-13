from django.shortcuts import render, HttpResponse
from .models import posts_model, categories_model

# Create your views here.

def blog(request):
    all_posts = posts_model.objects.all()
    all_categories = categories_model.objects.all()
    return render(request, 'blog.html', {'all_categories_key': all_categories, 'all_posts_key': all_posts})

def posts_filtrados(request, categories_model_id):
    category_filter = categories_model.objects.get(id=categories_model_id)
    all_posts_filtered = posts_model.objects.filter(categorias=category_filter)
    return render(request, 'filtro.html', {
        "category_filter_key": category_filter,
        "all_posts_filtered_key": all_posts_filtered,
    })


