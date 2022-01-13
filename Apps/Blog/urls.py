from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog' ),
    path('categoria/<int:categories_model_id>/', views.posts_filtrados, name="categ"),
]
